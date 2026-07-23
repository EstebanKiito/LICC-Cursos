#include <iostream>
#include <cassert>
#include <string>
#include <functional>
#include <algorithm>
#include <vector>
#include <utility>
#include "../src/dccfarm.hpp"
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>
#include <print>

using namespace std;

/* STABLE */
struct Stable {
    string name;
    int capacity;
};

function<bool(const Stable&, const Stable&)> sort_by_name = [](const Stable& s1, const Stable& s2) {
    return s1.name <= s2.name;
};

function<bool(const Stable&, const Stable&)> sort_by_capacity = [](const Stable& s1, const Stable& s2) {
    return s1.capacity <= s2.capacity;
};

function<bool(const Stable&)> is_name_upper = [](const Stable& s) { 
    for (auto &c : s.name) {
        if (!isupper(c))
            return false;
    }
    return true;
};
function<bool(const Stable&)> is_stable_small = [](const Stable& s) { 
    return s.capacity < 10;
};
function<bool(const Stable&)> is_capacity_even = [](const Stable& s) { 
    return (s.capacity % 2) == 0; 
};
function<string(const Stable&)> get_stable_name = [](const Stable& s) { 
    return s.name; 
};

vector<Stable> stables = {
    {"DCC", 80},
    {"cai", 12},
    {"CCC", 5}
};

/* auxilary variables */


vector<string> animals = {"cow", "chicken", "sheep"};
vector<int> first_five = {1, 2, 3, 4, 5};
vector<string> crops = {"maiz", "trigo", "choclo", "arroz"};
vector<int> empty_vector;
vector<string> names = {"otis", "pig", "pip", "duke"};
vector<bool> bools = {true, true, false, false, true};
vector<bool> true_bools = {true, true, true, true, true};


function<string(const string&)> to_upper = [](const string &s) {
    string r = s;
    for (char &c : r) c = toupper(static_cast<unsigned char>(c));
    return r;
};

function<int(const int&)> add_1 = [](const int &i) { 
    return i + 1; 
};

function<int(const int&, const int&)> adder = [](const int &a, const int &b) { 
    return a + b; 
};

function<int(const int&)> times_2 = [](const int &i) { 
    return i * 2; 
};

function<int(const int&)> square = [](const int &i) { 
    return i * i; 
};

function<int(const int&)> power = [](const int &i) { 
    return 1 << i; 
};

function<bool(const string&)> is_too_long = [](const string &s) { 
    return s.size() > 4; 
};
function<bool(const int&)> is_even = [](const int &i) { 
    return (i % 2) == 0; 
};
function<bool(const int&)> is_positive  = [](const int& n) { 
    return n > 0; 
};

function<bool(const string&, const string&)> sort_strings 
    = [](const string& s1, const string& s2) { return s1 <= s2; };

function<bool(const int&, const int&)> sort_ints 
    = [](const int& a, const int& b) { return a <= b; };

/* TESTS */

void test_farm_map() {
    assert(farm_map(animals, to_upper) == ((vector<string>){"COW", "CHICKEN", "SHEEP"}));
    assert(farm_map(first_five, square) == ((vector<int>){1, 4, 9, 16, 25}));
    assert(farm_map(first_five, power) == ((vector<int>){2, 4, 8, 16, 32}));
    assert(farm_map(farm_map(first_five, square), power) == ((vector<int>){2, 16, 512, 65536, 33554432}));
    assert(farm_map(stables, ((get_stable_name))) == ((vector<string>){"DCC", "cai", "CCC"}));
}

void test_farm_filter() {
    
    assert(farm_filter(crops, is_too_long) == ((vector<string>){"trigo", "choclo", "arroz"}));
    assert((farm_filter(stables, is_stable_small).size()) == 1);
    assert((farm_filter(stables, is_stable_small)[0].name) == "CCC");
    assert(farm_filter(first_five, is_even) == ((vector<int>){2, 4}));
}

void test_farm_foldl() {
    function<int(int,int)> sum = [](int acc, int x){ return acc + x; };
    function<int(int,int)> sub = [](int acc, int x){ return acc - x; };
    function<bool(bool,bool)> are_true = [](bool acc, bool x){ return acc && x; };
    function<string(string,string)> sum_string = [](string acc, string x){ return acc + x; };
    assert(farm_foldl(first_five, 0, sum) == 15);
    assert(farm_foldl(first_five, 1, sub) == -14);
    assert(farm_foldl(empty_vector, 100, sum) == 100);
    assert(farm_foldl(bools, true, are_true) == false);
    assert(farm_foldl(names, string("freddy"), sum_string) == "freddyotispigpipduke");
}

void test_farm_foldr() {
    function<int(int,int)> sum = [](int acc, int x){ return acc + x; };
    function<int(int,int)> sub = [](int acc, int x){ return acc - x; };
    function<bool(bool,bool)> are_true = [](bool acc, bool x){ return acc && x; };
    function<string(string,string)> sum_string = [](string acc, string x){ return acc + x; };
    assert(farm_foldr(first_five, 0, sum) == 15);
    assert(farm_foldr(first_five, 1, sub) == -14);
    assert(farm_foldr(first_five, 0, sub) == -15);
    assert(farm_foldr(true_bools, true, are_true) == true);
    assert(farm_foldr(names, string("freddy"), sum_string) == "freddydukepippigotis");
}

void test_predicates_1() {
    function<bool(const int&)> get_true = [](const bool& x) { return x || (!x); };
    function<bool(const int&)> get_false  = [](const bool& x) { return x && (!x); };
    assert(andP(get_true, get_true)(true) == true);
    assert(andP(get_true, get_false)(true) == false);
    assert(andP(get_false, get_true)(true) == false);
    assert(andP(get_false, get_false)(true) == false);
    assert(orP(get_true, get_true)(true) == true);
    assert(orP(get_true, get_false)(true) == true);
    assert(orP(get_false, get_true)(true) == true);
    assert(orP(get_false, get_false)(true) == false);
    assert(notP(get_true)(true) == false);
    assert(notP(get_false)(true) == true);
}

void test_predicates_2() {
    assert(andP(is_even, is_positive)(4) == true);
    assert(andP(is_even, is_positive)(-2) == false);
    assert(orP(is_even, is_positive)(-3) == false);
    assert(orP(is_even, is_positive)(-2) == true);
    assert(notP(is_even)(3) == true);
    assert(notP(is_even)(2) == false);
}

void test_predicates_3() {
    Stable dcc = stables[0];
    Stable cai = stables[1];
    Stable ccc = stables[2];
    
    assert(andP(is_capacity_even, is_name_upper)(dcc));
    assert(andP(is_capacity_even, notP(is_stable_small))(dcc));
    assert(orP(is_capacity_even, is_stable_small)(ccc));
    assert(orP(notP(is_name_upper), notP(is_capacity_even))(ccc));
    assert((notP(andP(is_name_upper, is_capacity_even)))(ccc));
    assert((andP(orP(is_name_upper, is_capacity_even), notP(is_stable_small)))(cai));
}

void test_streams_1() {
    assert(take(from(1), 5) == first_five);
    assert(take(from(5), 5) == (vector<int>{5, 6, 7, 8, 9}));
    assert((take(lazy_map(from(1), square), 3) == vector<int>{1, 4, 9}));
    assert((take(lazy_filter(from(1), is_even), 5) == vector<int>{2, 4, 6, 8, 10}));
    assert(take(lazy_map(from(1), power), 8) == (vector<int>{2, 4, 8, 16, 32, 64, 128, 256}));
}

void test_streams_2() {
    assert(take(fibonacci(1), 7) == (vector<int>{1, 1, 2, 3, 5, 8, 13}));
    assert(take(fibonacci(14), 5) == (vector<int>{21, 34, 55, 89, 144}));
    assert(take(even_squares(1), 3) == (vector<int>{4, 16, 36}));
    assert(take(even_squares(36), 3) == (vector<int>{36, 64, 100}));
    assert(take(primes(1), 5) == (vector<int>{2, 3, 5, 7, 11}));
    assert(take(primes(10), 5) == (vector<int>{11, 13, 17, 19, 23}));
}

void test_query_api() {
    assert((Query(first_five)
        .where(is_even)
        .to_list())
        == (vector<int>{2, 4}));
    assert((Query(animals)
        .where(is_too_long)
        .to_list())
        == (vector<string>{"chicken", "sheep"}));
    assert((Query(crops)
        .where(is_too_long)
        .order_by(sort_strings)
        .to_list())
        == (vector<string>{"arroz", "choclo", "trigo"}));
    assert((Query(names)
        .where(is_too_long)
        .to_list())
        == (vector<string>{}));
    assert((Query(names)
        .select(to_upper)
        .order_by(sort_strings)
        .to_list())
        == (vector<string>{"DUKE", "OTIS", "PIG", "PIP"}));
    assert((Query(stables)
        .where(is_name_upper)
        .select(get_stable_name)
        .order_by(sort_strings).to_list()) 
        == (vector<string>{"CCC", "DCC"}));
}

void test_matchers() {
    assert(match_string("matcha latte")("matcha latte") == true);
    assert(match_string("matcha latte")("matcha mocha") == false);

    assert((match_concat(
        match_string("matcha"), match_string(" latte"))("matcha latte")
    ) == true);

    auto mocha_espresso = match_choice(
        match_string("mocha"), match_string("espresso"));
    assert(mocha_espresso("espresso") == true);
    assert(mocha_espresso("mocha") == true);
    assert(mocha_espresso("macchiato") == false);

    auto many_a = match_many(match_string("a"));
    assert(many_a("aaa") == true);
    assert(many_a("") == true);
    assert(many_a("aaab") == false);

    auto anyc = match_any();
    assert(anyc("a") == true);
    assert(anyc("aa") == false);
}

void test_compose() {
    assert(compose(add_1, times_2)(3) == 7);
    assert(compose(times_2, add_1)(3) == 8);
    assert(compose(to_upper, get_stable_name)(stables[1]) == "CAI");
    assert(pipe((vector<function<int(int)>>{ times_2, add_1 }))(3) == 7);
    assert(pipe((vector<function<int(int)>>{ add_1, times_2 }))(3) == 8);
    assert(pipe((vector<function<int(int)>>{ times_2, times_2, times_2, times_2, times_2, times_2, times_2, times_2 }))(1) == 256);
}
void test_curry(){
    assert(curry_twice(adder)(2)(3) == 5);
    assert(uncurry(curry_twice(adder))(2,3) == 5);
}

void test_sorting(){
    function<bool(const int&,const int&)> desc_sort = [](int a,int b){ return a > b; };
    assert(sort_by<int>(vector<int>{3,1,4,2}, sort_ints) == (vector<int>{1, 2, 3, 4}));
    auto desc = sort_by(vector<int>{3,1,4,2}, desc_sort);
    assert(desc == (vector<int>{4, 3, 2, 1}));
}

void test_publisher() {
    Publisher publisher;
    bool flag = false;
    publisher.subscribe("event", "set_flag", [&](){ flag = true; });
    publisher.publish("event");
    assert(flag == true);
    int i = 0;
    auto add_i = [&](){ i++; };
    publisher.subscribe("event", "add", add_i);
    publisher.subscribe("event", "add", add_i);
    publisher.subscribe("event", "add", add_i);
    publisher.publish("event");
    assert(i == 3);
    publisher.unsubscribe("event", "add");
    publisher.publish("event");
    assert(i == 3);
}

int main() {
    auto exit_code = 0;
    auto tests = {
        test_farm_map,
        test_farm_filter,
        test_farm_foldl,
        test_farm_foldr,
        test_predicates_1,
        test_predicates_2,
        test_predicates_3,
        test_streams_1,
        test_streams_2,
        test_query_api,
        test_matchers,
        test_compose,
        test_curry,
        test_sorting,
        test_publisher
    };
    for (auto test : tests) {
        pid_t process_id = fork();
        if (process_id == 0) {
            try { 
                test();
                return 0;
            }
            catch (const exception& e) {
                cerr << "Error: " << e.what() << endl;
                return 1;
            }
        }
        else {
            int status = 0;
            waitpid(process_id, &status, 0);
            exit_code = (exit_code || WEXITSTATUS(status));
        }
        
    }
    return exit_code;
}