from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from PIL import Image
from io import BytesIO

app = FastAPI()

@app.get('/')
def read_root():
    return {"message": "Bonjour, ceci est le point de terminaison racine"}
from segmentation import segment_everything

@app.post("/segment-image")
async def segment_image(file: UploadFile = File(..., description="L'image à traiter", form=True)):
    try:
        contents = await file.read()
        image = Image.open(BytesIO(contents)).convert("RGB")
        print("Image chargée avec succès")

        # Appel de la fonction de segmentation
        segmentation_result = segment_everything(image=image)

        if isinstance(segmentation_result, type(Image.Image())):
            print("Segmentation effectuée avec succès")

            # Convertir le résultat en JSON et le renvoyer
            return JSONResponse(content={"segmentation_result": "Segmentation effectuée avec succès"})
        else:
            raise ValueError("segmentation_result n'est pas du type attendu")

    except Exception as e:
        print(f"Erreur lors du traitement de l'image : {str(e)}")
        return JSONResponse(content={"error": f"Erreur lors du traitement de l'image : {str(e)}"}, status_code=500)


