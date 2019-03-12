import os
import re
import pickle
from os import path, listdir

# global settings
# -----------------------------------------------------------------------------
class Config(object):
    # intermediate processing folders
    arxiv_dir =os.path.join('data', 'pdf', 'arxiv')
    db_dir   = os.path.join('data','db.p')
    pArxiv_dir   = os.path.join('data','pArxiv')
    pdf_dir = os.path.join('data', 'pdf')
    txt_dir = os.path.join('data', 'txt')
    models_dir   = os.path.join('models')
    p_dir   = os.path.join('data','p')
    #prefix = path.expanduser("~/gdrive/research/nlp/data/")
    prefix = path.expanduser("/home/mcaserta/research/nlp/matheur")
    prefixDict = path.expanduser("/home/mcaserta/research/nlp/data")
    vocab_folder = "google_vocab/"
    mappingFile = "mapping.csv"
    mappingArxiv = "mappingArxiv.csv"
    ngramsFile = "myngrams.txt"
    acronsFile = "myacrons.txt"
    specialFile = "myspecialwords.txt"
    nameModel  = "doc2vec.model"

    biblioTitle = ["Bibliography", "References", "Acknowledgments", "Acknowledgements"]

