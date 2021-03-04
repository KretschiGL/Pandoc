pandoc -t json -o Tabs.json --filter ./tab-filter.py -f markdown ./Tabs.md
pandoc -t docx -o Tabs.docx --filter ./tab-filter.py -f markdown ./Tabs.md