#!/bin/bash

PROBLEMNR=$1
PROBLEM="problem${PROBLEMNR}.py"

2to3 ${PROBLEM} -p
pep8 ${PROBLEM}
pylint ${PROBLEM}
time python $PROBLEM
rm *.pyc
