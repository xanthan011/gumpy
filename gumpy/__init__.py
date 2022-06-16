# import all gumpy submodules that should be loaded automatically
import gumpy.gumpy.classification
import gumpy.gumpy.data
import gumpy.gumpy.plot
import gumpy.gumpy.signal
import gumpy.gumpy.utils
import gumpy.gumpy.features
import gumpy.gumpy.split

# fetch into gumpy-scope so that users don't have to specify the entire
# namespace
from gumpy.gumpy.classification import classify

# retrieve the gumpy version (required for package manager)
from gumpy.gumpy.version import __version__
