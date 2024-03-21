# Welcome to the world of Python
# Author: black1277
# https://github.com/black1277/cinema4d/blob/main/scripts/ReflectionMaterial.py

import c4d

def main():
    
    # начинаем создавать с нуля
    material = c4d.BaseMaterial(c4d.Mmaterial)
    material.SetName('MyMaterial')
    material[c4d.MATERIAL_USE_COLOR] = False # канал цвета отключаем
    material[c4d.MATERIAL_USE_REFLECTION] = True # канал отражений активируем
    
    # сначала удаляем все слои из канала отражений
    material.RemoveReflectionAllLayers() 
    material[c4d.REFLECTION_LAYER_GLOBAL_SEPARATE_PASS]=False # отдельный проход для канала
    material[c4d.REFLECTION_LAYER_GLOBAL_REFLECTION]= 1. # глобальное отражение для всех слоев
    material[c4d.REFLECTION_LAYER_GLOBAL_SPECULAR] = 1. # глобальный глянец
    # *************** первый слой *******************************   
    layerFirst = material.AddReflectionLayer() # добавляем новый слой
    layerFirst.SetName('ORENNAYAR')
    IDF = layerFirst.GetDataID() # получили ID слоя
    material[IDF + c4d.REFLECTION_LAYER_MAIN_DISTRIBUTION] = c4d.REFLECTION_DISTRIBUTION_ORENNAYAR # тип слоя
    material[IDF + c4d.REFLECTION_LAYER_MAIN_ADDITIVE] = 4 # ослабление - металл
    material[IDF + c4d.REFLECTION_LAYER_MAIN_VALUE_ORENNAYAR] = .25 # шероховатость
    material[IDF + c4d.REFLECTION_LAYER_MAIN_SHADER_ORENNAYAR] = None # текстура
    material[IDF + c4d.REFLECTION_LAYER_MAIN_VALUE_REFLECTION] = .85 # интенсивность отражения
    material[IDF + c4d.REFLECTION_LAYER_MAIN_SHADER_REFLECTION] = None # текстура
    material[IDF + c4d.REFLECTION_LAYER_MAIN_COLORED_REFLECTION] = False # цветной
    material[IDF + c4d.REFLECTION_LAYER_MAIN_VALUE_SPECULAR] = .15 # интенсивность глянца
    material[IDF + c4d.REFLECTION_LAYER_MAIN_SHADER_SPECULAR] = None # текстура
    material[IDF + c4d.REFLECTION_LAYER_MAIN_COLORED_SPECULAR] = False # цветной
    material[IDF + c4d.REFLECTION_LAYER_MAIN_VALUE_BUMP] = .95 # интенсивность рельефа
    material[IDF + c4d.REFLECTION_LAYER_MAIN_SHADER_BUMP] = None # текстура
    material[IDF + c4d.REFLECTION_LAYER_MAIN_VALUE_BUMP_MODE] = 1 # карта рельефа
    material[IDF + c4d.REFLECTION_LAYER_MAIN_SHADER_BUMP_CUSTOM] = None # текстура
    material[IDF + c4d.REFLECTION_LAYER_MAIN_VALUE_BUMP_BUMP] = .24 # интенсивность
    material[IDF + c4d.REFLECTION_LAYER_MAIN_VALUE_BUMP_MIPMAP] = True
    #
    #
    #
    # *************** второй слой *******************************
    my_layer = material.AddReflectionLayer() # добавляем новый слой
    my_layer.SetName('BECKMANN')

    ID = my_layer.GetDataID()
    material[ID + c4d.REFLECTION_LAYER_MAIN_DISTRIBUTION] = c4d.REFLECTION_DISTRIBUTION_BECKMANN
    # c4d.REFLECTION_DISTRIBUTION_SIMPLE = 0
    # c4d.REFLECTION_DISTRIBUTION_SPECULAR_BLIN = 1
    # c4d.REFLECTION_DISTRIBUTION_BECKMANN = 2   
    # c4d.REFLECTION_DISTRIBUTION_GGX   = 3
    # c4d.REFLECTION_DISTRIBUTION_PHONG	= 4
    # c4d.REFLECTION_DISTRIBUTION_WARD = 5
    # c4d.REFLECTION_DISTRIBUTION_ANISOTROPIC = 6
    # c4d.REFLECTION_DISTRIBUTION_LAMBERTIAN  = 7
    # c4d.REFLECTION_DISTRIBUTION_ORENNAYAR   = 8
    # c4d.REFLECTION_DISTRIBUTION_IRAWAN = 9
    material[ID + c4d.REFLECTION_LAYER_MAIN_ADDITIVE] = 0
    #0 усредненное  c4d.REFLECTION_ADDITIVE_MODE_AVG
    #2 максимальное  c4d.REFLECTION_ADDITIVE_MODE_MAX	
    #3 дополнительное c4d.REFLECTION_ADDITIVE_MODE_ADD
    #4 металл  c4d.REFLECTION_ADDITIVE_MODE_METAL
    material[ID + c4d.REFLECTION_LAYER_MAIN_VALUE_ROUGHNESS] = .25
    material[ID + c4d.REFLECTION_LAYER_MAIN_SHADER_ROUGHNESS] = None

    material[ID + c4d.REFLECTION_LAYER_MAIN_VALUE_REFLECTION] = .65
    material[ID + c4d.REFLECTION_LAYER_MAIN_SHADER_REFLECTION] = None
    material[ID + c4d.REFLECTION_LAYER_MAIN_COLORED_REFLECTION]= False
    material[ID + c4d.REFLECTION_LAYER_MAIN_VALUE_SPECULAR] = .1
    material[ID + c4d.REFLECTION_LAYER_MAIN_SHADER_SPECULAR] = None
    material[ID + c4d.REFLECTION_LAYER_MAIN_COLORED_SPECULAR] = False
    material[ID + c4d.REFLECTION_LAYER_MAIN_VALUE_BUMP] = .8
    material[ID + c4d.REFLECTION_LAYER_MAIN_SHADER_BUMP] = None
    material[ID + c4d.REFLECTION_LAYER_MAIN_VALUE_BUMP_MODE] = 1 # 0 умолчание c4d.REFLECTION_BUMP_MODE_DEFAULT, 1 - рельеф c4d.REFLECTION_BUMP_MODE_BUMP, 2 нормали c4d.REFLECTION_BUMP_MODE_NORMAL
    material[ID + c4d.REFLECTION_LAYER_MAIN_SHADER_BUMP_CUSTOM] = None
    material[ID + c4d.REFLECTION_LAYER_MAIN_VALUE_BUMP_BUMP] = .2
    material[ID + c4d.REFLECTION_LAYER_MAIN_VALUE_BUMP_MIPMAP] = True
    #Color
    material[ID + c4d.REFLECTION_LAYER_COLOR_COLOR] = c4d.Vector(1,0.85,0.61)
    material[ID + c4d.REFLECTION_LAYER_COLOR_BRIGHTNESS] = .95
    material[ID + c4d.REFLECTION_LAYER_COLOR_TEXTURE] = None
    material[ID + c4d.REFLECTION_LAYER_COLOR_MIX_MODE] = 3 # 0 - 3
    material[ID + c4d.REFLECTION_LAYER_COLOR_MIX_STRENGTH] = .92
    #Mask
    material[ID + c4d.REFLECTION_LAYER_TRANS_BRIGHTNESS] = 1. # интенсивность маски, 
    # она же - интенсивность слоя в стопке слоев
    material[ID + c4d.REFLECTION_LAYER_TRANS_COLOR] = c4d.Vector(0.15,0.85,0.61)
    material[ID + c4d.REFLECTION_LAYER_TRANS_TEXTURE] = None
    material[ID + c4d.REFLECTION_LAYER_TRANS_MIX_MODE]= 2  # 0 - 3
    material[ID + c4d.REFLECTION_LAYER_TRANS_MIX_STRENGTH] = .86
    #Frenel
    material[ID + c4d.REFLECTION_LAYER_FRESNEL_MODE] = 1 # 0 нет c4d.REFLECTION_FRESNEL_NONE, 1 диэлектрик c4d.REFLECTION_FRESNEL_DIELECTRIC , 2 проводник c4d.REFLECTION_FRESNEL_CONDUCTOR
    if material[ID + c4d.REFLECTION_LAYER_FRESNEL_MODE] == 1: # если диэлектрик
        material[ID + c4d.REFLECTION_LAYER_FRESNEL_PRESET] = 17 # 0-17
        #c4d.REFLECTION_FRESNEL_DIELECTRIC_CUSTOM					0				///< Custom.
        #c4d.REFLECTION_FRESNEL_DIELECTRIC_ASPHALT					1				///< Asphalt.
        #c4d.REFLECTION_FRESNEL_DIELECTRIC_BEER						2				///< Beer.
        #c4d.REFLECTION_FRESNEL_DIELECTRIC_DIAMOND					3				///< Diamond.
        #c4d.REFLECTION_FRESNEL_DIELECTRIC_EMERALD					4				///< Emerald.
        #c4d.REFLECTION_FRESNEL_DIELECTRIC_ETHANOL					5				///< Ethanol.
        #c4d.REFLECTION_FRESNEL_DIELECTRIC_GLASS					6				///< Glass.
        #c4d.REFLECTION_FRESNEL_DIELECTRIC_JADE						7				///< Jade.
        #c4d.REFLECTION_FRESNEL_DIELECTRIC_MILK						8				///< Milk.
        #c4d.REFLECTION_FRESNEL_DIELECTRIC_OIL_VEGETABLE	        9				///< Oil (Vegetable).
        #c4d.REFLECTION_FRESNEL_DIELECTRIC_PEARL					10			///< Pearl.
        #c4d.REFLECTION_FRESNEL_DIELECTRIC_PET						11			///< PET.
        #c4d.REFLECTION_FRESNEL_DIELECTRIC_PLEXIGLASS		    	12			///< Plexiglas.
        #c4d.REFLECTION_FRESNEL_DIELECTRIC_RUBY						13			///< Ruby.
        #c4d.REFLECTION_FRESNEL_DIELECTRIC_SAPPHIRE		    		14			///< Sapphire.
        #c4d.REFLECTION_FRESNEL_DIELECTRIC_WATER					15			///< Water.
        #c4d.REFLECTION_FRESNEL_DIELECTRIC_WATER_ICE		    	16			///< Water (Ice).
        #c4d.REFLECTION_FRESNEL_DIELECTRIC_WHISKEY					17			///< Whiskey.
        material[ID + c4d.REFLECTION_LAYER_FRESNEL_VALUE_STRENGTH] = .85
        material[ID + c4d.REFLECTION_LAYER_FRESNEL_SHADER_STRENGTH] = None
        material[ID + c4d.REFLECTION_LAYER_FRESNEL_VALUE_IOR] = 1.25
        material[ID + c4d.REFLECTION_LAYER_FRESNEL_SHADER_IOR] = None
        material[ID + c4d.REFLECTION_LAYER_FRESNEL_INVERTED] = False
        material[ID + c4d.REFLECTION_LAYER_FRESNEL_OPAQUE] = False
    if material[ID + c4d.REFLECTION_LAYER_FRESNEL_MODE] == 2:# если проводник
        material[ID + c4d.REFLECTION_LAYER_FRESNEL_METAL] = 0
        #c4d.REFLECTION_FRESNEL_METAL_CUSTOM							0				///< Custom.
        #c4d.REFLECTION_FRESNEL_METAL_ALUMINUM							1				///< Aluminum.
        #c4d.REFLECTION_FRESNEL_METAL_BERYLLIUM					    	2				///< Beryllium.
        #c4d.REFLECTION_FRESNEL_METAL_CHROMIUM							3				///< Chromium.
        #c4d.REFLECTION_FRESNEL_METAL_COPPER							4				///< Copper.
        #c4d.REFLECTION_FRESNEL_METAL_COPPER_OXIDE			    		5				///< Copper Oxide.
        #c4d.REFLECTION_FRESNEL_METAL_GOLD								6				///< Gold.
        #c4d.REFLECTION_FRESNEL_METAL_IRIDIUM							7				///< Iridium.
        #c4d.REFLECTION_FRESNEL_METAL_IRON								8				///< Iron.
        #c4d.REFLECTION_FRESNEL_METAL_LITHIUM							9				///< Lithium.
        #c4d.REFLECTION_FRESNEL_METAL_MAGNESIUM_OXIDE	        		10			///< Magnesium Oxide.
        #c4d.REFLECTION_FRESNEL_METAL_MERCURY							11			///< Mercury.
        #c4d.REFLECTION_FRESNEL_METAL_NICKEL							12			///< Nickel.
        #c4d.REFLECTION_FRESNEL_METAL_NIOBIUM							13			///< Niobium.
        #c4d.REFLECTION_FRESNEL_METAL_POTASSIUM			    			14			///< Potassium.
        #c4d.REFLECTION_FRESNEL_METAL_RHODIUM							15			///< Rhodium.
        #c4d.REFLECTION_FRESNEL_METAL_SELENIUM							16			///< Selenium.
        #c4d.REFLECTION_FRESNEL_METAL_SILICON_CARBIDE		        	17			///< Silicon Carbide.
        #c4d.REFLECTION_FRESNEL_METAL_SILVER							18			///< Silver.
        #c4d.REFLECTION_FRESNEL_METAL_SODIUM							19			///< Sodium.
        #c4d.REFLECTION_FRESNEL_METAL_TANTALUM							20			///< Tantalum.
        #c4d.REFLECTION_FRESNEL_METAL_TELLURIUM				    		21			///< Telluride.
        #c4d.REFLECTION_FRESNEL_METAL_TIN_TELLURIDE			        	22			///< Tin Telluride.
        #c4d.REFLECTION_FRESNEL_METAL_TITANIUM_NITRIDE	        		23			///< Titanium Nitride.
        #c4d.REFLECTION_FRESNEL_METAL_TUNGSTEN							24			///< Tungsten.
        #c4d.REFLECTION_FRESNEL_METAL_VANADIUM							25			///< Vanadium.
        #c4d.REFLECTION_FRESNEL_METAL_CUSTOM_NBM				   		26			///< Custom value for NBM materials.        
        material[ID + c4d.REFLECTION_LAYER_FRESNEL_VALUE_STRENGTH] = .75
        material[ID + c4d.REFLECTION_LAYER_FRESNEL_SHADER_STRENGTH] = None
        material[ID + c4d.REFLECTION_LAYER_FRESNEL_VALUE_ETA] = 1.15
        material[ID + c4d.REFLECTION_LAYER_FRESNEL_SHADER_ETA] = None
        material[ID + c4d.REFLECTION_LAYER_FRESNEL_VALUE_ABSORP] = 2.05
        material[ID + c4d.REFLECTION_LAYER_FRESNEL_SHADER_ABSORP] = None
        material[ID + c4d.REFLECTION_LAYER_FRESNEL_INVERTED] = False
        material[ID + c4d.REFLECTION_LAYER_FRESNEL_OPAQUE] = False
    # ********************************************************************

    doc.InsertMaterial(material) # вставим материал в документ
    doc.SetActiveMaterial(material) # сделаем его активным
    c4d.EventAdd()

if __name__=='__main__':
    main()