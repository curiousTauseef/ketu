# -*- coding: utf-8 -*-

__version__ = "0.1.0"

try:
    __TURNSTILE_SETUP__  # NOQA
except NameError:
    __TURNSTILE_SETUP__ = False

if not __TURNSTILE_SETUP__:
    __all__ = ["Pipeline", "Download", "PreparedDownload", "Inject",
               "Prepare", "Detrend",
               "GPLikelihood", "OneDSearch", "TwoDSearch", "PeakDetect",
               "FeatureExtract", "Validate"]

    from .pipeline import Pipeline
    from .download import Download, PreparedDownload
    from .inject import Inject
    from .prepare import Prepare
    from .detrend import Detrend
    from .likelihood import GPLikelihood
    from .one_d_search import OneDSearch
    from .two_d_search import TwoDSearch
    from .peak_detect import PeakDetect
    from .feature_extract import FeatureExtract
    from .dv import Validate
