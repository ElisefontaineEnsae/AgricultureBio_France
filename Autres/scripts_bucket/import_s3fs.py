import s3fs

fs = s3fs.S3FileSystem(client_kwargs={"endpoint_url": "https://minio.lab.sspcloud.fr"})

MY_BUCKET = "elisefontaine"
fs.ls(MY_BUCKET)

# Créer le dossier diffusion à la racine du bucket
diffusion_folder = 'elisefontaine/diffusion'
if not fs.exists(diffusion_folder):
    fs.mkdir(diffusion_folder)
    print(f"Dossier '{diffusion_folder}' créé avec succès.")
else:
    print(f"Dossier '{diffusion_folder}' existe déjà.")

# Chemin local du fichier volumineux
local_file = (
    '/home/onyxia/work/data_geopackage'
)

# Chemin distant dans S3 (dossier diffusion)
remote_file = 'elisefontaine/diffusion/data_geopackage'


# Transférer le fichier vers le dossier diffusion
fs.put(local_file, remote_file)
print(f"Fichier '{local_file}' transféré vers '{remote_file}'.")

