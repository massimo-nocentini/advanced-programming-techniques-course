
COMPILER = lualatex
TEXFILE = doc

compile:
	${COMPILER} ${TEXFILE}.tex

compile-ps:
	latex ${TEXFILE}.tex
	dvips ${TEXFILE}.dvi

compile-bib:
	rm ${TEXFILE}.aux
	${COMPILER} ${TEXFILE}.tex
	bibtex ${TEXFILE}
	${COMPILER} ${TEXFILE}.tex
	${COMPILER} ${TEXFILE}.tex

