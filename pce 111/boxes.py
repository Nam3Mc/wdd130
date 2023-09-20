
print ( 'To help you calculating boxes needed, please!')
itens = int ( input ('Enter the number of items:' ) )
itens_x_boxes = int ( input ( 'Enter the number of items per box: ' ) )
import math

boxes_needed = ( itens / itens_x_boxes ) 

print ( f' For {itens} items, packing {itens_x_boxes} items in each box, you will need {math.ceil(boxes_needed)} boxes.' )