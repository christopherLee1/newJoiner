#!/usr/bin/env python3
import sys
import argparse

#class JoinerFile(self):
#   """class that represents a joinerFile. subclasses represent different properties"""

def parseArgs():
   """parse command line"""
   parser = argparse.ArgumentParser()
   parser.add_argument('--identifier', help='just validate given identifer')
   parser.add_argument('--database', help='validate given database, accounts for case where db is secondary key for hgFixed style tracks.')
   parser.add_argument('--keys', help='validate keys')
   parser.add_argument('--times', help='check update times')
   parser.add_argument('--tableCoverage', help='check that all tables are mentioned in joiner file')
   parser.add_argument('--dbCoverage', help='check that all databases are mentioned in joiner file')
   args = parser.parse_args()
   if len(sys.argv) < 2:
      parser.print_help()
   else:
      return args

# parse joiner file for mysql queries to run
def parseJoinerFile(self, identifier, database, keys, times):
   """Read in a joiner file and look for relationships"""
   pass

def validate_identifier():
   """check all defined relationships for given identifier"""
   pass

def validate_database():
   """find and check all identifiers with db as primary or foreign key"""
   pass

def validate_keys():
   """for all identifiers, check foreign keys"""
   pass

def validate_times():
   """for all identifiers, check times"""
   pass

def check_tableCoverage():
   """check that all tables are mentioned in joiner file"""
   pass

def check_dbCoverage():
   """check that all databses are mentioned in joiner file"""
   pass

# run appropriate mysql queries
# examples
# this query checks name fields from ci2.xenoRefGene for matches in acc field of hgFixed.gbCdnaInfo
#hgsql -e "select count(name) from ci2.xenoRefGene inner join hgFixed.gbCdnaInfo on xenoRefGene.name = gbCdnaInfo.acc"

# to check a minCheck like the following:
#identifier vegaPseudoGeneZfishName typeOf=vegaPseudoZfishName dependency
#"Link together Zebrafish VEGA predicted gene structure additional information"
#    $danRer.vegaPseudoGene.name
#    $danRer.vegaInfoZfish.transcriptId minCheck=0.004
# hgsql -e "select count(vegaPseudoGene.name) from danRer5.vegaPseudoGene inner join danRer5.vegaInfoZfish on vegaPseudoGene.name = vegaInfoZfish.transcriptId"
# the minCheck means 4% of items in vegaInfoZfish.transcriptId must be in vegaPseudoGene
options = parseArgs()

