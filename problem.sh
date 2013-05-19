#!/bin/bash

PROBLEMNR=$1
PROBLEM="problem${PROBLEMNR}.py"

2to3 ${PROBLEM} -p
pep8 ${PROBLEM}
pylint ${PROBLEM}
time pypy $PROBLEM
rm *.pyc
