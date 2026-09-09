#!/bin/bash

# 1. Automatically check and sync project dependencies
bundle check || bundle install

# 2. Open the website in your default browser
open "http://localhost:4000"

# 3. Start the Jekyll development server
bundle exec jekyll serve
