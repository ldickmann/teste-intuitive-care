import pdfplumber
import re
import logging


def extract_table_data(pdf_path):
    """Extrai dados de tabelas de um PDF"""
    table_data = []
