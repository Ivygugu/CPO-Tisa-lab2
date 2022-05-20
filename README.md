# Tisa-lab2-variant2

This repo is the Lab2 of Computational Process Organization in ITMO, 2022 spring.

## Project structure description

* `DynamicArray.py` -- includes class `DynamicArray` with methods `__eq__` and `__str__`,
 class `DynamicArrayIterator` with `__iter__` and `__next__`,
 and functions `cons`, `remove`, `length`, `member`, `reverse`, `set`,
 `to_list`, `from_list`,
 `find`, `filter`, `map`, `reduce`, `iterator`, `empty`, and `concat`.

* `DynamicArray_test.py` -- unit and PBT tests for classes and functions in `DynamicArray.py`.

## Contribution

* Chen Biao(1377681089@qq.com)
  * Implement the `DynamicArray.py`
  * Write `README.md`
  * Source code framework construction

* Guo Zhaoxin(zhaoxin_guo@163.com)
  * Implement the `DynamicArray_test.py`
  * Write `README.md`
  * Created GitHub repository

## Features

* `cons(lst, v)`: copy array `lst` as a new one and add
 a new element `v` to the end of the new.
 If `capacity == length`,it will allocate a new chunk of memory
 by user-specified growing factor.
* `remove(lst, pos)`: keep `lst` constant, return a new array
 that remove element at `pos`.
* `length(lst)`: return the length of `lst`.
* `member(lst, v)`: return a boolean indicating whether
 the element `v` is a member of `lst`.
* `reverse(lst)`:  keep `lst` constant, return a reverse array of `lst`.
* `set(lst, pos, v)`: copy array `lst` as a new one and
 set a new element `v` at `pos`.
* `to_list(lst)`: convert `lst` to built-in `list`.
* `from_list(list)`: convert from built-in `list`.
* `find(lst, pred)`: find element by specific predicate, return a boolean value.
* `filter(pred, lst)`: keep `lst` constant, filter data structure by specific predicate.
* `map(func, *iters)`: map elements of arrays by specific function,
 return a new array and keep `*iters` constant.
* `reduce(func, lst, initializer=None)`: process elements of the array `lst` to
 build a return value by
 specific function.
* `iterator(lst)`: return an iterator of `lst`.
* `empty()`: return an empty instance of `DynamicArray`.
* `concat(lst1, lst2)`: keep `lst1` and `lst2` constant,
 return a new array of two arrays concatenate.

## Changelog

* 20.5.2022 - 2
  * update `README.md`
* 14.5.2022 - 1
  * update `DynamicArray.py` and `DynamicArray_test.py`
* 11.5.2022 - 0
  * Initial.

## Design notes

### Compare mutable and immutable implementation

* Mutable Infrastructure
  * Fix problems more quickly. Rather than needing to create a new
server from scratch, IT staff gets to know each server on a
"personal" level, making diagnoses faster.
  * The infrastructure can more precisely fit the specific needs
of the applications that are running on the server.
  * Updates are usually faster and can be adapted to each individual server. 

* Immutable Infrastructure
  * Discrete versioning means tracking and rollbacks are much easier.
IT department can keep tabs on each new server or virtual machine
as it is deployed.
  * Testing is easier to run thanks to the consistency in
configurations between different servers.
  * Predictable state since the infrastructure is never modified,
reducing complexity.
  * Safe thread code in a multi-threaded environment meaning mutation
is almost nonexistent.
  * Supports DevOps and cloud computing including virtualization and
the high number of interdependent elements.
  * Eliminates configuration drift, since there are no changes,
there is no drift.
