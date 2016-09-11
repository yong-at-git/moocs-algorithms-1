#! /usr/bin/env python3


class ListUtils:

    @staticmethod
    def get_first_half(input_list):
        length = len(input_list)

        return [] if (length == 0) else input_list[0:length // 2]

    @staticmethod
    def get_second_half(input_list):
        length = len(input_list)

        return [] if (length == 0) else input_list[length // 2:length]
