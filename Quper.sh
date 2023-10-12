#!/bin/bash

files=(
    "completeness/compliance_of_disclosure.py"
    "timeliness/timeline.py"
    "availability/get_external_link.py"
    "availability/get_language_type.py"
    "readability/doubleNeg_obscure_qualifiers.py"
    "readability/main_idea_location.py"
    "readability/readability.py"
)

for file in "${files[@]}"; do
    result=$(python3 "$file")
    
    echo "Result of $file:"
    echo "-------------------------"
    echo "$result"
    echo "-------------------------"
    echo ""
done

