pandoc -t json -o Options.json --filter ./option-filter.py -f markdown ./Options.md
pandoc -t docx -o Options.docx --filter ./option-filter.py -f markdown ./Options.md
