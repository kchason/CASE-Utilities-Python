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

import pathlib
import typing

import rdflib

NS_KB = rdflib.Namespace("http://example.org/kb/")
NS_SH = rdflib.SH
NS_UCO_CORE = rdflib.Namespace("https://unifiedcyberontology.org/ontology/uco/core#")
NS_UCO_OBSERVABLE = rdflib.Namespace(
    "https://unifiedcyberontology.org/ontology/uco/observable#"
)

_ground_truth_set = typing.Set[
    typing.Tuple[rdflib.URIRef, rdflib.URIRef, rdflib.URIRef]
]


def _compute_ground_truth_set(filename: str) -> _ground_truth_set:
    graph = rdflib.Graph()
    graph.parse(str(pathlib.Path(__file__).parent / filename))
    conforms: typing.Optional[bool] = None
    for triple in graph.triples((None, NS_SH.conforms, None)):
        conforms = triple[2].toPython()
    assert conforms == False

    computed: _ground_truth_set = set()
    for result in graph.query(
        """\
SELECT ?nFocusNode ?nResultPath ?nSourceConstraintComponent
WHERE {
  ?nResult
    a sh:ValidationResult ;
    sh:focusNode ?nFocusNode ;
    sh:resultPath ?nResultPath ;
    sh:sourceConstraintComponent ?nSourceConstraintComponent ;
    .
}
"""
    ):
        computed.add(result)
    return computed


def test_deep_read() -> None:
    expected_node_path_constraints: _ground_truth_set = {
        (
            NS_KB["file-facet-1"],
            NS_UCO_OBSERVABLE.sizeInBytes,
            NS_SH.DatatypeConstraintComponent,
        )
    }
    computed_node_path_constraints: _ground_truth_set = _compute_ground_truth_set(
        "deep_validation.ttl"
    )
    assert expected_node_path_constraints == computed_node_path_constraints


def test_shallow_read() -> None:
    """
    Note that at the time of this writing (CASE 0.5.0, UCO 0.7.0), the sizeInBytes range error is not detected when a node class is not defined.
    """
    # TODO - UCO will need class-independent rdfs:range tests.
    expected_node_path_constraints: _ground_truth_set = {
        (
            NS_KB["provenance-record-1"],
            NS_UCO_CORE.object,
            NS_SH.ClassConstraintComponent,
        )
    }
    computed_node_path_constraints: _ground_truth_set = _compute_ground_truth_set(
        "shallow_validation.ttl"
    )
    assert expected_node_path_constraints == computed_node_path_constraints
