How do I visualise a gbXML file?
================================

Using the *render* method
-------------------------

gbXML files can be rendered in 3D using matplotlib. The code below does this using the :py:func:`~xgbxml.xgbxml.Campus.render` method of the :py:class:`~xgbxml.xgbxml.Campus` class.

.. code-block:: python

   from lxml import etree
   import xgbxml

   parser = xgbxml.get_parser('0.37')   

   tree = etree.parse('gbXML_TRK.xml', parser)  # file available on GitHub here: https://github.com/GreenBuildingXML/Sample_gbXML_Files
   gbxml = tree.getroot()

   ax=gbxml.Campus.render()
   ax.set_title('gbXML_TRK.xml')

   fig=ax.figure
   fig.set_size_inches(16, 16)
   fig.savefig('gbXML_TRK_render.png')
   
.. image:: _static/gbXML_TRK_render.png