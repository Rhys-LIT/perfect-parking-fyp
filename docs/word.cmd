REM pandoc -f markdown -t docx "report-analysis-and-design.md" -o "report-analysis-and-design.docx"
pandoc -f docx -t markdown "thesis.docx" -o "thesis.md" --extract-media ./images/thesis