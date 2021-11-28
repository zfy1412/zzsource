#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author: Zhan Shi
Time  : 2021/5/12 13:49
"""


class Grid(object):
    """
    Class Grid
    """

    def __init__(self, survey_grid_width, public_key, p1=None, p2=None):
        """
        Grid initialize
        :param p1: the first point
        :param p2: the second point
        """
        self.p1 = p1
        self.p2 = p2

        self.sgw = survey_grid_width
        self.pk = public_key

        if p2 is None:
            self.tg = list()
        else:
            self.tg = self._create_trajectory_grid()
        self.sg = self._create_survey_grid()

    @staticmethod
    def _grid_number(point, x, y, grid_width):
        """
        Calculate grid number
        |0,  1| 1,  1 |2,  1|
        |0,  0|(1,  0)|2,  0|
        |0, -1| 1, -1 |2, -1|
        :param point: node point
        :param x: iteration x
        :param y: iteration y
        :param grid_width: grid width
        :return: grid number
        """
        grid_number = list()

        for i in range(x[0], x[1] + 1):
            for j in range(y[0], y[1] + 1):
                number = int(point[0]) // grid_width + i + (int(point[1]) // grid_width + j) * 36000000
                grid_number.append(number)

        return grid_number

    def _create_trajectory_grid(self):
        """
        Create trajectory grid signature
        :return: trajectory grid signature
        """

        # ====================Built-in Method 1 START==================== #
        def __get_node(increment, boundary, temp, _k=None, _b=None):
            """
            Get node of the coordinate
            :param increment: start point
            :param boundary: end point
            :param temp: function temp
            :param _k: param k
            :param _b: param b
            :return: coordinate node
            """

            # ====================Built-in Method 2 START==================== #
            def __boundary_determine_(_point, grid_width):
                """
                Map boundary determine
                :param _point: determine point
                :param grid_width: determine grid width
                :return: grid number
                """
                if _point[0] == 36000000:
                    x = (0, 0)
                elif _point[0] % grid_width == 0 and _point[0] != 0:
                    x = (0, 1)
                else:
                    x = (1, 1)

                if _point[1] == 36000000:
                    y = (-1, -1)
                elif _point[1] % grid_width == 0 and _point[1] != 0:
                    y = (-1, 0)
                else:
                    y = (0, 0)

                return self._grid_number(_point, x, y, grid_width)

            # =====================Built-in Method 2 END===================== #
            _survey_grid_number = list()

            while increment <= boundary:
                if temp == 'x':
                    point = [increment, _k * increment + _b]
                    if increment % self.sgw == 0:
                        _survey_grid_number.extend(__boundary_determine_(point, self.sgw))

                elif temp == 'y':
                    point = [(increment - _b) / _k, increment]
                    if increment % self.sgw == 0:
                        _survey_grid_number.extend(__boundary_determine_(point, self.sgw))

                else:
                    point = [temp, increment]
                    if increment % self.sgw == 0:
                        _survey_grid_number.extend(__boundary_determine_(point, self.sgw))

                increment += (self.sgw // 10)

            return _survey_grid_number

        # =====================Built-in Method 1 END===================== #
        survey_grid_number = list()

        delta_point = [self.p2[0] - self.p1[0], self.p2[1] - self.p1[1]]
        if delta_point[0] != 0:
            k = delta_point[1] / delta_point[0]
            b = self.p1[1] - (k * self.p1[0])

            if delta_point[0] > 0:
                _survey_grid_number_x = __get_node(self.p1[0], self.p2[0], 'x', k, b)
            else:
                _survey_grid_number_x = __get_node(self.p2[0], self.p1[0], 'x', k, b)

            if delta_point[1] > 0:
                _survey_grid_number_y = __get_node(self.p1[1], self.p2[1], 'y', k, b)
            elif delta_point[1] < 0:
                _survey_grid_number_y = __get_node(self.p2[1], self.p1[1], 'y', k, b)
            else:
                _survey_grid_number_y = list()

        else:
            _survey_grid_number_x = list()

            if delta_point[1] > 0:
                _survey_grid_number_y = __get_node(self.p1[1], self.p2[1], self.p1[0])
            elif delta_point[1] < 0:
                _survey_grid_number_y = __get_node(self.p2[1], self.p1[1], self.p1[0])
            else:
                _survey_grid_number_y = __get_node(self.p1[1], self.p1[1], self.p1[0])

        survey_grid_number.extend(_survey_grid_number_x + _survey_grid_number_y)

        if not survey_grid_number:
            survey_grid_number = self._grid_number(self.p1, (1, 1), (0, 0), self.sgw)

        return survey_grid_number

    def _create_survey_grid(self):
        """
        Create survey grid signature
        :return: survey grid signature
        """
        if self.p1[0] == 0:
            x = (1, 1)
        elif self.p1[0] == 36000000:
            x = (0, 0)
        elif self.p1[0] < self.sgw:
            x = (1, 2)
        elif self.p1[0] % self.sgw == 0 or self.p1[0] > 36000000 - self.sgw:
            x = (0, 1)
        else:
            x = (0, 2)

        if self.p1[1] == 0:
            y = (0, 0)
        elif self.p1[1] == 36000000:
            y = (-1, -1)
        elif self.p1[1] < self.sgw:
            y = (0, 1)
        elif self.p1[1] % self.sgw == 0 or self.p1[1] > 36000000 - self.sgw:
            y = (-1, 0)
        else:
            y = (-1, 1)

        return self._grid_number(self.p1, x, y, self.sgw)
