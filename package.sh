#!/bin/bash
# prepare a source code package

pip install --upgrade --target package/ requests
cd package
zip -r9 ${OLDPWD}/package.zip .
cd ${OLDPWD}
zip -g package.zip function.py
zip -g package.zip s3.py

rm -rf package