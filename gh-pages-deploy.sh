#!/bin/bash

git checkout --orphan gh-pages

echo "Building started..."
npm run build

git --work-tree "dist" add --all
git --work-tree "dist" commit -m "gh-pages deploy"

echo "Pushing to gh-pages..."
git push origin gh-pages --force

rm -r "dist"

git checkout -f vue
git branch -D gh-pages

echo "Successfully deployed, check your settings"