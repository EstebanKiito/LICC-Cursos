#pragma once

#include <vector>
#include <functional>
#include <string>
#include <cstddef>

using namespace std;

template<typename T, typename M>
vector<M> farm_map(const vector<T>& lst, function<M(const T&)> f);

template<typename T>
vector<T> farm_filter(const vector<T>& lst, function<bool(const T&)> f);

template<typename T, typename Acc>
Acc farm_foldl(const vector<T>& lst, Acc init, function<Acc(Acc, T)> f);

template<typename T, typename Acc>
Acc farm_foldr(const vector<T>& lst, Acc init, function<Acc(Acc, T)> f);

template<typename T>
function<bool(const T&)> andP(function<bool(const T&)> p, function<bool(const T&)> q);

template<typename T>
function<bool(const T&)> orP(function<bool(const T&)> p, function<bool(const T&)> q);

template<typename T>
function<bool(const T&)> notP(function<bool(const T&)> p);

using Stream = function<int()>;

Stream from(int start);

Stream lazy_map(Stream s, function<int(const int&)> f);

Stream lazy_filter(Stream s, function<bool(const int&)> pred);

vector<int> take(Stream s, int k);

Stream even_squares(int start);

Stream primes(int start);

Stream fibonacci(int start);

template<typename T>
class Query {
public:
    Query(const vector<T>& src);

    Query<T> where(function<bool(const T&)> cond) const;

    template<typename U>
    Query<U> select(function<U(const T&)> proj) const;

    Query<T> order_by(function<bool(const T&, const T&)> cmp) const;

    vector<T> to_list() const;
private:
    vector<T> items;
};

using Matcher = function<bool(const string&)>;

Matcher match_string(const string& s);
Matcher match_concat(Matcher p, Matcher q);
Matcher match_choice(Matcher p, Matcher q);
Matcher match_many(Matcher p);
Matcher match_any();

template<typename A, typename B, typename C>
function<C(const A&)> compose(function<C(const B&)> f, function<B(const A&)> g);

template<typename T>
function<T(T)> pipe(const vector<function<T(T)>>& lst);

template<typename A, typename B, typename R>
function< function<R(B)>(A) > curry_twice(function<R(A,B)> f);

template<typename A, typename B, typename R>
function<R(A,B)> uncurry(function< function<R(B)>(A) > f);

template<typename T>
vector<T> sort_by(const vector<T>& lst, function<bool(const T&, const T&)> cmp);

class Publisher {
public:
    using Handler = function<void()>;
    void subscribe(const string& event_name, const string& handler_name, Handler handler);
    void unsubscribe(const string& event_name, const string& handler_name);
    void publish(const string& event_name);
};

#include "dccfarm.tpp"