# Troubleshooting

If you encounter problems starting a node, ensure that the required
dependencies listed in ``requirements.txt`` are installed.  Many examples rely
on the ``websockets`` package which is not part of the Python standard
library.

When debugging network issues it can be helpful to start the node with the
``ENHANCED_NETWORK_DEBUG`` environment variable set to ``1``.  This enables
verbose logging throughout the stack.
