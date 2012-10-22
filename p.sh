#!/bin/bash

PROBLEMNR="003"
PROBLEM="problem${PROBLEMNR}.py"

time python $PROBLEM
2to3 ${PROBLEM} -p
pep8 ${PROBLEM}
pylint ${PROBLEM}

rm *.pyc
