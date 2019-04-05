import os
import re
import pickle
from os import path, listdir

# global settings
# -----------------------------------------------------------------------------
class Config(object):
    # intermediate processing folders
    arxiv_dir =os.path.join('data', 'pdf', 'arxiv')
    #  arxiv_dir =os.path.join('data', 'pdf', 'arxiv2')
    db_dir   = os.path.join('data','db.p')
    pArxiv_dir   = os.path.join('data','pArxiv')
    #  pArxiv_dir   = os.path.join('data','pArxiv2')
    pdf_dir = os.path.join('data', 'pdf')
    txt_dir = os.path.join('data', 'txt')
    models_dir   = os.path.join('models')
    p_dir   = os.path.join('data','p')
    pAbstract_dir   = os.path.join('data','pAbstract')
    #prefix = path.expanduser("~/gdrive/research/nlp/data/")
    prefix = path.expanduser("/home/mcaserta/research/matheur")
    prefixDict = path.expanduser("/home/mcaserta/research/nlp/data")
    vocab_folder = "google_vocab/"
    mappingFile = "mapping.csv"
    mappingArxiv = "mappingArxiv.csv"
    distanceMatrixFile = "distanceMatrix.csv"
    sortedDIstanceFile = "sortedDistance.csv"
    ngramsFile = "myngrams.txt"
    acronsFile = "myacrons.txt"
    specialFile = "myspecialwords.txt"
    nameModel  = "doc2vec.model"

    biblioTitle = ["Bibliography", "References", "Acknowledgments",
    "Acknowledgements", 'BIBLIOGRAPHY', 'REFERENCES', 'ACKNOWLEDGEMENTS',
    'ACKNOWLEDGMENTS', 'Reference', 'REFERENCE']

    abstractTitle = ["Abstract", "ABSTRACT", "Summary", "SUMMARY", "a b s t r a c t", "A B S T R A C T"]

