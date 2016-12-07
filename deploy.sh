#!/bin/bash
mkdir public/static
mv public/*.* public/static
mv public/js/ public/static
mv public/img/ public/static
mv public/css/ public/static
rm -rf public/base
cp app.yaml public/app.yaml
cd public
appcfg.py update app.yaml  
# This is a comenty sort of line
#chemica brothers
