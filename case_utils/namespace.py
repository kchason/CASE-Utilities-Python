#!/usr/bin/env python3

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

"""
This module provides importable constants for namespaces.

To use, add "from case_utils.namespace import *".  Namespace variables starting with "NS_" are imported.  As needs are demonstrated in CASE tooling (both in case_utils and from downstream requests), namespaces will also be imported from rdflib for a consistent "NS_*" spelling.
"""

import rdflib  # type: ignore

NS_SH = rdflib.SH
NS_RDF = rdflib.RDF
NS_XSD = rdflib.XSD

NS_CASE_INVESTIGATION = rdflib.Namespace(
    "https://ontology.caseontology.org/case/investigation/"
)
NS_UCO_ACTION = rdflib.Namespace("https://unifiedcyberontology.org/ontology/uco/action#")
NS_UCO_CORE = rdflib.Namespace("https://unifiedcyberontology.org/ontology/uco/core#")
NS_UCO_LOCATION = rdflib.Namespace("https://unifiedcyberontology.org/ontology/uco/location#")
NS_UCO_OBSERVABLE = rdflib.Namespace(
    "https://unifiedcyberontology.org/ontology/uco/observable#"
)
NS_UCO_TYPES = rdflib.Namespace("https://unifiedcyberontology.org/ontology/uco/types#")
NS_UCO_VOCABULARY = rdflib.Namespace(
    "https://unifiedcyberontology.org/ontology/uco/vocabulary#"
)
