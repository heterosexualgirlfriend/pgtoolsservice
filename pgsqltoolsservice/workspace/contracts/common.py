# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import pgsqltoolsservice.utils as utils


class Position:
    """
    Represents a point in the document
    Attributes:
        line:       0-based line number
        character:  0-based column number
    """

    @classmethod
    def from_data(cls, line: int, col: int):
        pos = cls()
        pos.line = line
        pos.character = col
        return pos

    @classmethod
    def from_dict(cls, dictionary: dict):
        return utils.serialization.convert_from_dict(cls, dictionary)

    def __init__(self):
        self.line: int = 0
        self.character: int = 0


class Range:
    """
    Represents a selection of the document
    Attributes:
        start:  The starting position of the range, inclusive
        end:    The ending position of the range, inclusive
    """

    @classmethod
    def from_data(cls, start_line: int, start_col: int, end_line: int, end_col: int):
        result = cls()
        result.start = Position.from_data(start_line, start_col)
        result.end = Position.from_data(end_line, end_col)
        return result

    @classmethod
    def from_dict(cls, dictionary: dict):
        return utils.serialization.convert_from_dict(cls, dictionary,
                                                     start=Position,
                                                     end=Position)

    def __init__(self):
        self.start: Position = None
        self.end: Position = None


class TextDocumentItem:
    """
    Defines a text document
    Attributes:
        uri:            The URI that uniquely identifies the path of the text document
        language_id:    Language of the document
        version:        The version of the document
        text:           Full content of the document
    """

    @classmethod
    def from_dict(cls, dictionary: dict):
        return utils.serialization.convert_from_dict(cls, dictionary)

    def __init__(self):
        self.uri: str = None
        self.language_id: str = None
        self.version: int = None
        self.text: str = None