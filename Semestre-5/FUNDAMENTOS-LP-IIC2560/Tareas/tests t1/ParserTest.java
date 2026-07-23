package com.iic2560;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.Arrays;
import java.util.List;

import com.iic2560.Nodes.NodeFactory;
import com.iic2560.Nodes.Ast;

class ParserTest {

    @Test
    void testParse1() throws ParseException {
        assertConstantsEquals(1);
    }

    @Test
    void testParse2() throws ParseException {
        assertConstantsEquals(5);
    }

    @Test
    void testParse3() throws ParseException {
        assertConstantsEquals(24);
    }

    @Test
    void testParse4() throws ParseException {
        assertConstantsEquals(52);
    }

    @Test
    void testParse5() throws ParseException {
        assertConstantsEquals(1234567890);
    }

    @Test 
    void testWrongParse1() throws ParseException {
        assertConstantsNotEquals(20, 5);
    }

    @Test 
    void testWrongParse2() throws ParseException {
        assertConstantsNotEquals(30, 1);
    }

    @Test 
    void testWrongParse3() throws ParseException {
        assertConstantsNotEquals(40, 2);
    }

    @Test 
    void testWrongParse4() throws ParseException {
        assertConstantsNotEquals(50, 3);
    }

    @Test 
    void testWrongParse5() throws ParseException {
        assertConstantsNotEquals(60, 61);
    }
    
    @Test
    void testSum() throws ParseException {

        assertParseEquals(
            "(2 + 3)", 
            sum(
                constant(2), 
                constant(3)));
    }
    
    @Test
    void testSub() throws ParseException {
        assertParseEquals(
            "( 24 - 36)", 
            sub(
                constant(24), 
                constant(36)));
    }
    
    @Test
    void testMult() throws ParseException {

        assertParseEquals(
            "(120 * 240 )", 
            mult(
                constant(120), 
                constant(240)));
    }
    
    @Test
    void testDiv() throws ParseException {

        assertParseEquals(
            "( 1 / 000 )", 
            div(
                constant(1), 
                constant(0)));
    }
    
    @Test
    void testDivSpaced() throws ParseException {
        assertParseEquals(
            "(                        57 / 1234567)", 
            div(
                constant(57), 
                constant(1234567)));
    }
    
    @Test
    void testTrees1() throws ParseException {
        assertParseEquals(
            "((20 / 10) + (1 / 2))", 
            sum(
                div(
                    constant(20), 
                    constant(10)),
                div(
                    constant(1), 
                    constant(2))));

    }
    
    @Test
    void testTrees2() throws ParseException {
        assertParseEquals(
            "((2 * 4) - (3 + (6 / 100)))", 
            sub(
                mult(
                    constant(2), 
                    constant(4)),
                sum(
                    constant(3),
                    div(
                        constant(6), 
                        constant(100)))));
    }
    
    @Test
    void testTrees3() throws ParseException {
        assertParseEquals(
            "(1 + (2 - (4 * (888 / 0))))", 
            sum(
                constant(1), 
                sub(
                    constant(2), 
                    mult(
                        constant(4), 
                        div(
                            constant(888), 
                            constant(0))))));
    }
    
    @Test
    void testTrees4() throws ParseException {
        assertParseEquals(
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
                    constant(2))));
    }

    @Test
    void testFormat() throws ParseException {
        assertParseEquals(
            "000001", 
            constant(1));
    }

    @Test
    void testParseErrors1() {
        assertParseError("(1)");
        assertParseError("()");
        assertParseError("-1");
        assertParseError("4.99");
        assertParseError("(2 ^ 8)");
    }

    @Test
    void testParseErrors2() {
        assertParseError("(1+100)");
        assertParseError("(2+ 8)");
        assertParseError("(20 +1)");
    }

    @Test
    void testParseErrors3() {
        assertParseError("e");
        assertParseError("ashdjaasgjkdhgfajd");
        assertParseError("(mish)");
    }

    @Test
    void testParseErrors4() {
        assertParseError("(1 + )");
        assertParseError("( - 1)");
        assertParseError("(2 * 3 / 4)");
        assertParseError("(8 * (2 / ))");
        assertParseError("(7 - ( * 5))");
    }

    @Test
    void testParseErrors5() {
        assertParseError("1234u3456");
        assertParseError("entre123numeros");
    }

    @Test
    void testParseErrors6() {
        assertParseError("(578 - 4567 * 982634 / 34783   )");
        assertParseError("(567 (8 - 7))");
        assertParseError("100(1)");
        assertParseError("56832 (35627) ");
    }

    @Test
    void testAmbiguity1() throws ParseException {

        assertParseTrees(
            "1 + 2", 
            new Ast[] { sum(constant(1), constant(2)) });
    }

    @Test
    void testAmbiguity2() throws ParseException {

        assertParseTrees(
            "1 + 2 * 3", 
            new Ast[] { 
                sum(constant(1), mult(constant(2), constant(3))),
                mult(sum(constant(1), constant(2)), constant(3)) });
    }

    @Test
    void testAmbiguity3() throws ParseException {

        assertParseTrees(
            "1 + 2 * 3 / 4", 
            new Ast[] { 
                sum(constant(1), mult(constant(2), div(constant(3), constant(4)))),
                sum(constant(1), div(mult(constant(2), constant(3)), constant(4))),
                mult(sum(constant(1), constant(2)), div(constant(3), constant(4))),
                div(sum(constant(1), mult(constant(2), constant(3))), constant(4)),
                div(mult(sum(constant(1), constant(2)), constant(3)), constant(4)) });
    }

    @Test
    void testBigAmbiguity() throws ParseException {
        Ast[] trees = new Ast[] { 
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
            sum(constant(1), sub(div(mult(constant(2), constant(3)), constant(4)), constant(5))) };
        
            assertParseTrees(
            "1 + 2 * 3 / 4 - 5", 
            trees);
    }

    void assertParseTrees(String program, Ast[] trees) throws ParseException{
        List<Ast> parseTrees = Arrays.asList(AmbiguousParser.parse(program));
        List<Ast> expectedTrees = Arrays.asList(trees);
        assertTrue(
            parseTrees.containsAll(expectedTrees), 
            "result tree " 
            + parseTrees.toString() 
            + " not contained in " 
            + expectedTrees.toString());
        assertTrue(
            expectedTrees.containsAll(parseTrees), 
            "expected tree " 
            + expectedTrees.toString() 
            + " not contained in " 
            + parseTrees.toString());
    }

    void assertParseError(String program) {
        assertThrows(ParseException.class, () -> Parser.parse(program));
    }

    void assertConstantsEquals(int constant) throws ParseException {
        assertParseEquals(
            String.valueOf(constant), 
            constant(constant));
    }

    void assertConstantsNotEquals(int parsedConstant, int constant) throws ParseException {
        assertParseNotEquals(
            String.valueOf(parsedConstant), 
            constant(constant));
    }

    void assertParseEquals(String program, Ast expected) throws ParseException {
        assertEquals(expected, Parser.parse(program));
    }

    void assertParseNotEquals(String program, Ast expected) throws ParseException {
        assertNotEquals(expected, Parser.parse(program));
    }

    Ast sum(Ast left, Ast right) {
        return NodeFactory.sum(left, right);
    }

    Ast sub(Ast left, Ast right) {
        return NodeFactory.sub(left, right);
    }

    Ast mult(Ast left, Ast right) {
        return NodeFactory.mult(left, right);
    }

    Ast div(Ast left, Ast right) {
        return NodeFactory.div(left, right);
    }

    Ast constant(int constant){
        return NodeFactory.constant(constant);
    }
}
