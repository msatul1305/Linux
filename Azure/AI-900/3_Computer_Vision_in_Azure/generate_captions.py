
import requests
import json
from dataclasses import dataclass, asdict

@dataclass
class Metadata:
    width: int
    height: int

@dataclass
class CaptionResult:
    text: str
    confidence: float

@dataclass
class AnalyzeResult:
    modelVersion: str
    metadata: Metadata
    captionResult: CaptionResult

@dataclass
class AnalyzeRequest:
    uri: str

class Caption:
    def generate_caption(self):
        # For prod environment, please find the endpoint and resource key of your computer vision resource from Azure portal.
        endpoint = "https://ai-ankitagrawalhero-4422.cognitiveservices.azure.com/"
        url = f"{endpoint}computervision/imageanalysis:analyze?features=caption&gender-neutral-caption=false&api-version=2023-10-01"
        key = ""

        headers = {
            'Ocp-Apim-Subscription-Key': key,
            'Content-Type': 'application/json; charset=utf-8'
        }

        # with image url
        image_url = "https://ai.azure.com/common/vision/imageCaptioning/ImageCaptioningSample6.png"

        # Create an instance of the AnalyzeRequest class
        analyze_request = AnalyzeRequest(uri=image_url)

        # Serialize the instance to a dictionary
        json_data = asdict(analyze_request)

        response = requests.post(url, headers=headers, json=json_data)
        response_content = response.text

        # Print the JSON response for debugging
        print("Response Content:", response_content)

        # Deserialize and print the result
        data = json.loads(response_content)
        try:
            deserialized_object = AnalyzeResult(
                modelVersion=data['modelVersion'],
                metadata=Metadata(**data['metadata']),
                captionResult=CaptionResult(**data['captionResult'])
            )

            print(f"Model Version: {deserialized_object.modelVersion}")
            print(f"Metadata - Width: {deserialized_object.metadata.width}, Height: {deserialized_object.metadata.height}")
            print(f"Caption: {deserialized_object.captionResult.text}, Confidence: {deserialized_object.captionResult.confidence}")
        except KeyError as e:
            print(f"KeyError: {e}. Please check the JSON response structure.")

# Usage example
if __name__ == "__main__":
    caption = Caption()
    caption.generate_caption()
