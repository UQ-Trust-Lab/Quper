#!/bin/bash

files=(
    "compliance_of_disclosure/compliance_of_disclosure.py"
    "timeliness/timeline.py"
    "availability/get_external_link.py"
    "availability/get_language_type.py"
    "readability/doubleNeg_obscure_qualifiers.py"
    "readability/main_idea_location.py"
    "readability/readability.py"
)

for file in "${files[@]}"; do
    cd "$(dirname "$file")"
    
    result=$(python3 "$(basename "$file")")
    
    echo "Result of $file:"
    echo "-------------------------"
    echo "$result"
    echo "-------------------------"
    echo ""
    
    cd - > /dev/null
done