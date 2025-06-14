# -*- coding: utf-8 -*-

"""This module is run as part of the package development, rather than by package users.

It reads the json versions of the xsd schemas, and then creates python modules
with classes for each element in the schema. 
These python classes are for element and attribute access, and are used in the 
lxml custom class parsers.

"""
import json, os


def generate_gbElements(version):
    ""
    
    with open(r'../schema_dicts/schema_dict_%s.json' % version.replace('.','_'),'r') as f:
        schema_dict=json.load(f)
    
    with open('gbElements_%s.py' % version.replace('.','_'),'w') as f:
        
        f.write('# gbElements_%s.py\n' % version)
        f.write('# autogenerated\n\n')
                
        for element_name,element_dict in schema_dict['elements'].items():
            #print(element_name)
            #pprint(element_dict)
            
            
            f.write('class %s_auto():\n' % element_name.replace('-','_'))
            f.write('\t"""'+'\n'.join(element_dict['annotations'])+'"""\n\n')
            
            for attribute_name,attribute_dict in element_dict['attributes'].items():
                
                if attribute_name=='id': continue
                
                # @property
                f.write('\t@property\n')
                f.write('\tdef %s(self):\n' % attribute_name)
                if attribute_dict['annotations']:
                    f.write('\t\t"""'+'\n'.join(attribute_dict['annotations'])+'"""\n')
                f.write("\t\treturn self.get_attribute('%s')\n\n\n" % attribute_name)
                
                # @.setter
                f.write('\t@%s.setter\n' % attribute_name)
                f.write('\tdef %s(self,value):\n' % attribute_name)
                f.write("\t\tself.set_attribute('%s',value)\n\n\n" % attribute_name)
            
            
            for child_name,child_dict in element_dict['child_elements'].items():
                
                # get child
                f.write('\t@property\n')
                f.write('\tdef %s(self):\n' % child_name.replace('-','_'))
                f.write("\t\treturn self.get_child('%s')\n\n\n" % child_name)
                
                # get children
                f.write('\t@property\n')
                f.write('\tdef %ss(self):\n' % child_name.replace('-','_'))
                f.write("\t\treturn self.get_children('%s')\n\n\n" % child_name)
                
                # add child
                f.write('\tdef add_%s(self,\n' % child_name.replace('-','_'))
                for attribute_name in schema_dict['elements'][child_name]['attributes']:
                    f.write('\t\t%s=None,\n' % attribute_name)
                f.write('\t\t):\n')
                f.write("\t\treturn self.add_child('%s',\n" % child_name)
                for attribute_name in schema_dict['elements'][child_name]['attributes']:
                    f.write('\t\t\t%s=%s,\n' % (attribute_name,attribute_name))
                f.write('\t\t\t)\n\n\n')
            
            f.write('\n')
                
# CREATE AND SAVE gbElements_X_XX.py files            
        
for fn in os.listdir(r'../schema_dicts'):
    if fn.startswith('_'):continue
    print(fn)
    version=fn[-9:-5]
    #print(version)
    generate_gbElements(version)

