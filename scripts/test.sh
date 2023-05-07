#!/bin/bash

if [ -z "$1" ]
then
   echo ">> Running all test cases"
    python3 -m pytest -s tests
else
   echo ">> Running single test case"
    python3 -m pytest -s $@
fi