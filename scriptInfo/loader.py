import pandas as pd
from faker import Faker
from collections import defaultdict 
from sqlalchemy import create_engine
from faker.providers import DynamicProvider

fake = Faker()
fake_data = defaultdict(list)
fake_data_empleado = defaultdict(list)
empresa_index = []
for _ in range(100):
    fake_data["nombre"].append( fake.unique.company() )
    fake_data["NIT"].append( fake.unique.numerify(text='#########') )
    empresa_index.append(fake_data["NIT"][-1])
    fake_data["temporalidadContrato"].append( fake.random_int(min=1, max=24, step=1) )
    fake_data["formatoDocumento"].append( fake.file_name(extension="pdf") )
    
df_fake_data = pd.DataFrame(fake_data)

for c in range(100):
    for _ in range(1000):
        fake_data_empleado["empresaAfiliada"].append( empresa_index[c] )
        fake_data_empleado["nombre"].append( fake.unique.name() )
        fake_data_empleado["sueldo"].append( fake.random_int(min=1000000, max=10000000, step=100000) )
        fake_data_empleado["inicioContrato"].append( fake.date_between(start_date='-1y', end_date='today') )
        fake_data_empleado["descuentoRealizado"].append( fake.random_int(min=10000, max=100000, step=2000) )
        fake_data_empleado["numeroDocumento"].append( fake.unique.numerify(text='#########') )
        fake_data_empleado["tipoDocumento"].append( fake.random_element(elements=('cedula','pasaporte')) )

df_fake_data_empleado = pd.DataFrame(fake_data_empleado)

engine = create_engine('postgresql+psycopg2://sprint_user:sprint2@10.128.0.4/sprint_db', echo=False)
#df_fake_data.to_sql('empresaAfiliada_empresaafiliada', con=engine, if_exists="append" ,index=False, method = 'multi')
df_fake_data_empleado.to_sql('empleado_empleado', con=engine, if_exists="append" ,index=False, method='multi')