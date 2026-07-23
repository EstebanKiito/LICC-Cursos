import unittest

from ..parser.parser import Parser
from ..parser.ambiguous_parser import AmbiguousParser
from ..nodes.node_factory import NodeFactory
from ..parser.parse_exception import ParseException

def constant(const):
    return NodeFactory.constant(const)

def sum(left, right):
    return NodeFactory.sum(left, right)

def sub(left, right):
    return NodeFactory.sub(left, right)

def mult(left, right):
    return NodeFactory.mult(left, right)

def div(left, right):
    return NodeFactory.div(left, right)

class ParserTest(unittest.TestCase):
    
    def test_constant(self):
        self.assertConstantsEquals(1)
    
    def test_constant_2(self):
        self.assertConstantsEquals(5)
    
    def test_constant_3(self):
        self.assertConstantsEquals(24)
    
    def test_constant_4(self):
        self.assertConstantsEquals(52)
    
    def test_constant_5(self):
        self.assertConstantsEquals(1234567890)

    def test_wrong_constant_1(self):
        self.assertConstantsNotEquals(20, 5)

    def test_wrong_constant_2(self):
        self.assertConstantsNotEquals(30, 1)

    def test_wrong_constant_3(self):
        self.assertConstantsNotEquals(40, 2)

    def test_wrong_constant_4(self):
        self.assertConstantsNotEquals(50, 3)

    def test_wrong_constant_5(self):
        self.assertConstantsNotEquals(60, 61)

    def test_sum(self):
        self.assertParseEquals(
            "(2 + 3)",
            sum(
                constant(2), 
                constant(3)))
        
    def test_sub(self):
        self.assertParseEquals(
            "( 24 - 36)",
            sub(
                constant(24), 
                constant(36)))
        
    def test_mult(self):
        self.assertParseEquals(
            "(120 * 240 )", 
            mult(
                constant(120), 
                constant(240)))
        
    def test_div(self):
        self.assertParseEquals(
            "( 1 / 000 )", 
            div(
                constant(1), 
                constant(0)))
        
    def test_div_spaced(self):
        self.assertParseEquals(
            "(                        57 / 1234567)", 
            div(
                constant(57), 
                constant(1234567))
        )
    
    def test_trees_1(self):
        self.assertParseEquals(
            "((20 / 10) + (1 / 2))", 
            sum(
                div(
                    constant(20), 
                    constant(10)),
                div(
                    constant(1), 
                    constant(2))))
        
    def test_trees_2(self):
        self.assertParseEquals(
            "((2 * 4) - (3 + (6 / 100)))", 
            sub(
                mult(
                    constant(2), 
                    constant(4)),
                sum(
                    constant(3),
                    div(
                        constant(6), 
                        constant(100)))))
        
    def test_trees_3(self):
        self.assertParseEquals(
            "(1 + (2 - (4 * (888 / 0))))", 
            sum(
                constant(1), 
                sub(
                    constant(2), 
                    mult(
                        constant(4), 
                        div(
                            constant(888), 
                            constant(0))))))
        
    def test_trees_4(self):
        self.assertParseEquals(
            "(1 + (((4 * ((1 * 6) + 5)) / 3) - 2))", 
            sum(
                constant(1), 
                sub(
                    div(
                        mult(
                            constant(4), 
                            sum(
                                mult(
                                    constant(1), 
                                    constant(6)), 
                                constant(5))), 
                        constant(3)), 
                    constant(2))))
    
    def test_format(self):
        self.assertParseEquals(
            "000001",
            NodeFactory.constant(1)
        )
    
    def test_parse_errors_1(self):
        self.assertParseError("(1)")
        self.assertParseError("()")
        self.assertParseError("-1")
        self.assertParseError("4.99")
        self.assertParseError("(2 ^ 8)")

    def test_parse_errors_2(self):
        self.assertParseError("(1+100)")
        self.assertParseError("(2+ 8)")
        self.assertParseError("(20 +1)")

    def test_parse_errors_3(self):
        self.assertParseError("e")
        self.assertParseError("ashdjaasgjkdhgfajd")
        self.assertParseError("(mish)")

    def test_parse_errors_4(self):
        self.assertParseError("(1 + )")
        self.assertParseError("( - 1)")
        self.assertParseError("(2 * 3 / 4)")
        self.assertParseError("(8 * (2 / ))")
        self.assertParseError("(7 - ( * 5))")

    def test_parse_errors_5(self):
        self.assertParseError("1234u3456")
        self.assertParseError("entre123numeros")

    def test_parse_errors_6(self):
        self.assertParseError("(578 - 4567 * 982634 / 34783   )")
        self.assertParseError("(567 (8 - 7))")
        self.assertParseError("100(1)")
        self.assertParseError("56832 (35627) ")

    def test_ambiguity_1(self):
        self.assertParseTrees("1 + 2", [sum(constant(1), constant(2))])

    def test_ambiguity_2(self):
        self.assertParseTrees(
            "1 + 2 * 3", 
            [sum(constant(1), mult(constant(2), constant(3))),
                mult(sum(constant(1), constant(2)), constant(3))])

    def test_ambiguity_3(self):
        self.assertParseTrees(
            "1 + 2 * 3 / 4", 
            [
                sum(constant(1), mult(constant(2), div(constant(3), constant(4)))),
                sum(constant(1), div(mult(constant(2), constant(3)), constant(4))),
                mult(sum(constant(1), constant(2)), div(constant(3), constant(4))),
                div(sum(constant(1), mult(constant(2), constant(3))), constant(4)),
                div(mult(sum(constant(1), constant(2)), constant(3)), constant(4))
                ])
        
    def test_big_ambiguity(self):
        expected_trees = [
                sub(sum(constant(1), mult(constant(2), div(constant(3), constant(4)))), constant(5)),
                sub(sum(constant(1), div(mult(constant(2), constant(3)), constant(4))), constant(5)),
                sub(mult(sum(constant(1), constant(2)), div(constant(3), constant(4))), constant(5)),
                sub(div(sum(constant(1), mult(constant(2), constant(3))), constant(4)), constant(5)),
                sub(div(mult(sum(constant(1), constant(2)), constant(3)), constant(4)), constant(5)),
                div(sum(constant(1), mult(constant(2), constant(3))), sub(constant(4), constant(5))),
                div(mult(sum(constant(1), constant(2)), constant(3)), sub(constant(4), constant(5))),
                mult(sum(constant(1), constant(2)), div(constant(3), sub(constant(4), constant(5)))),
                mult(sum(constant(1), constant(2)), sub(div(constant(3), constant(4)), constant(5))),
                sum(constant(1), mult(constant(2), div(constant(3), sub(constant(4), constant(5))))),
                sum(constant(1), mult(constant(2), sub(div(constant(3), constant(4)), constant(5)))),
                sum(constant(1), div(mult(constant(2), constant(3)), sub(constant(4), constant(5)))),
                sum(constant(1), sub(mult(constant(2), div(constant(3), constant(4))), constant(5))),
                sum(constant(1), sub(div(mult(constant(2), constant(3)), constant(4)), constant(5)))
            ]
    
        self.assertParseTrees(
            "1 + 2 * 3 / 4 - 5",
            expected_trees
        )

    def assertParseTrees(self, program:str, expected_trees:list):
        parse_trees = AmbiguousParser.parse(program)

        self.assertTrue(all(tree in expected_trees for tree in parse_trees), 
            f"result tree {parse_trees} not contained in {expected_trees}")

        self.assertTrue(all(tree in parse_trees for tree in expected_trees), 
            f"expected tree {expected_trees} not contained in {parse_trees}")

    def assertParseError(self, program:str):
        self.assertRaises(ParseException, lambda: Parser.parse(program))

    def assertConstantsEquals(self, const:int):
        self.assertParseEquals(str(const), constant(const))

    def assertConstantsNotEquals(self, parsed_const:int, const:int):
        self.assertParseNotEquals(str(parsed_const), constant(const) )

    def assertParseEquals(self, program:str, expected):
        self.assertEqual(expected, Parser.parse(program))

    def assertParseNotEquals(self, program:str, expected):
        self.assertNotEqual(expected, Parser.parse(program))


if __name__ == "__main__":
    unittest.main()