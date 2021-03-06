# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GisProgrammierungCSFTFF
                                 A QGIS plugin
 Das Plugin analysiert DGMs und reale Punktwolken auf folgende geometrischen Alogrithmen: "Konvexe Hülle", "Punkt-in-Polygon-Test" und dem "Ear-Clipping-Algorithmus". Die Ergebnisse werden visualisert und einem Performancevergleich (m/s) unterzogen. Hierbei wird eine große Anzahl von Geoobjekten (> 1.000.000) in eine relationale und Objektdatenbank gespeichert und eingelesen. 
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-01-04
        copyright            : (C) 2021 by Czarnach Simone, Feicht Tamara, Folger Florian
        email                : czarnach@hm.edu, Klein6@hm.edu, ffolger@hm.edu
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load GisProgrammierungCSFTFF class from file GisProgrammierungCSFTFF.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .gis_programmierung_cs_ft_ff import GisProgrammierungCSFTFF
    return GisProgrammierungCSFTFF(iface)
