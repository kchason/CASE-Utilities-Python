#!/usr/bin/make -f

# This software was developed at the National Institute of Standards
# and Technology by employees of the Federal Government in the course
# of their official duties. Pursuant to title 17 Section 105 of the
# United States Code this software is not subject to copyright
# protection and is in the public domain. NIST assumes no
# responsibility whatsoever for its use by other parties, and makes
# no guarantees, expressed or implied, about its quality,
# reliability, or any other characteristic.
#
# We would appreciate acknowledgement if the software is used.

SHELL := /bin/bash

top_srcdir := $(shell cd ../../../.. ; pwd)

case_srcdir := $(top_srcdir)/dependencies/CASE

tests_srcdir := $(top_srcdir)/tests

RDF_TOOLKIT_JAR := $(case_srcdir)/lib/rdf-toolkit.jar

all: \
  deep_kb.ttl \
  deep_validation.ttl \
  shallow_validation.ttl \
  shallow_kb.ttl

check: \
  deep_kb.ttl \
  deep_validation.ttl \
  shallow_validation.ttl \
  shallow_kb.ttl
	source $(tests_srcdir)/venv/bin/activate \
	  && pytest \
	    --log-level=DEBUG

clean:
	@rm -f \
	  *.ttl

# *_kb.ttl aggregates the input files for visual inspection in one format.
deep_kb.ttl: \
  $(RDF_TOOLKIT_JAR) \
  $(tests_srcdir)/.venv.done.log \
  $(tests_srcdir)/src/glom_graph.py \
  input_directory/deep/deep_1.ttl \
  input_directory/shallow_1.ttl \
  input_directory/shallow_2.json
	rm -f _$@ __$@
	source $(tests_srcdir)/venv/bin/activate \
	  && python3 $(tests_srcdir)/src/glom_graph.py \
	    __$@ \
	    input_directory/deep/deep_1.ttl \
	    input_directory/shallow_1.ttl \
	    input_directory/shallow_2.json
	java -jar $(RDF_TOOLKIT_JAR) \
	  --inline-blank-nodes \
	  --source __$@ \
	  --source-format turtle \
	  --target _$@ \
	  --target-format turtle
	rm __$@
	mv _$@ $@

# With respect to conformance, the validation files are XFAILs.  The Python tests confirm precisely how the validation fails.
deep_validation.ttl: \
  $(RDF_TOOLKIT_JAR) \
  $(tests_srcdir)/.venv.done.log \
  $(top_srcdir)/case_utils/case_validate/__init__.py \
  input_directory/deep/deep_1.ttl \
  input_directory/shallow_1.ttl \
  input_directory/shallow_2.json
	rm -f _$@ __$@
	source $(tests_srcdir)/venv/bin/activate \
	  && case_validate \
	    --debug \
	    --format turtle \
	    --inference none \
	    --output __$@ \
	    --recursive \
	    input_directory \
	    ; rc=$$? ; test 1 -eq $$rc
	test -s __$@
	java -jar $(RDF_TOOLKIT_JAR) \
	  --inline-blank-nodes \
	  --source __$@ \
	  --source-format turtle \
	  --target _$@ \
	  --target-format turtle
	rm __$@
	mv _$@ $@

shallow_kb.ttl: \
  $(RDF_TOOLKIT_JAR) \
  $(tests_srcdir)/.venv.done.log \
  $(tests_srcdir)/src/glom_graph.py \
  input_directory/shallow_1.ttl \
  input_directory/shallow_2.json
	rm -f _$@ __$@
	source $(tests_srcdir)/venv/bin/activate \
	  && python3 $(tests_srcdir)/src/glom_graph.py \
	    __$@ \
	    input_directory/shallow_1.ttl \
	    input_directory/shallow_2.json
	java -jar $(RDF_TOOLKIT_JAR) \
	  --inline-blank-nodes \
	  --source __$@ \
	  --source-format turtle \
	  --target _$@ \
	  --target-format turtle
	rm __$@
	mv _$@ $@

shallow_validation.ttl: \
  $(RDF_TOOLKIT_JAR) \
  $(tests_srcdir)/.venv.done.log \
  $(top_srcdir)/case_utils/case_validate/__init__.py \
  input_directory/shallow_1.ttl \
  input_directory/shallow_2.json
	rm -f _$@ __$@
	source $(tests_srcdir)/venv/bin/activate \
	  && case_validate \
	    --debug \
	    --format turtle \
	    --inference none \
	    --output __$@ \
	    input_directory \
	    ; rc=$$? ; test 1 -eq $$rc
	test -s __$@
	java -jar $(RDF_TOOLKIT_JAR) \
	  --inline-blank-nodes \
	  --source __$@ \
	  --source-format turtle \
	  --target _$@ \
	  --target-format turtle
	rm __$@
	mv _$@ $@
