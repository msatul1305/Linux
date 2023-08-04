using Azure;
using Azure.Storage.Blobs;
using Azure.Storage.Blobs.Models;
using System;
using System.Collections.Generic;
using System.IO;
using System.Threading.Tasks;

namespace Pluralsight.PropertiesMetadataApp
{
  class Program
  {
    // TODO: Add your connection string here
    private static readonly string _connectionString = "";

    private static readonly string _blobContainerName = "authors";
    private static readonly string _blobName = "thomas.html";

    private async static Task Main(string[] args)
    {
      try
      {
        BlobClient blobClient = await CreateContainerAndUploadBlobAsync();

        await SetBlobPropertiesAsync(blobClient);

        await GetBlobPropertiesAsync(blobClient);

        await SetBlobMetadataAsync(blobClient);

        await GetBlobMetadataAsync(blobClient);

        Console.WriteLine();
        Console.WriteLine($"Press ENTER to delete blob container '{_blobContainerName}'");
        Console.ReadLine();

        await DeleteContainerAsync();
      }
      catch (RequestFailedException exception)
      {
        Console.WriteLine($"Error: {exception.ErrorCode}");

        if (exception.ErrorCode == "ContainerBeingDeleted")
        {
          Console.WriteLine($"> The container '{_blobContainerName}' is currently being deleted.");
          Console.WriteLine("> This takes usually up to 30 seconds.");
          Console.WriteLine("> Wait a bit and run the program again.");
        }
      }
      catch (Exception exception)
      {
        Console.WriteLine(exception.Message);
      }
    }

    private static async Task<BlobClient> CreateContainerAndUploadBlobAsync()
    {
      // 1. Create the Blob Container
      BlobServiceClient blobServiceClient = new BlobServiceClient(_connectionString);

      BlobContainerClient blobContainerClient =
          blobServiceClient.GetBlobContainerClient(_blobContainerName);

      Console.WriteLine($"1. Creating blob container '{_blobContainerName}'");

      await blobContainerClient.CreateIfNotExistsAsync(PublicAccessType.BlobContainer);

      // 2. Upload a Blob
      BlobClient blobClient = blobContainerClient.GetBlobClient(_blobName);

      Console.WriteLine($"2. Uploading blob '{blobClient.Name}'");
      Console.WriteLine($"   > {blobClient.Uri}");

      using FileStream fileStream = File.OpenRead("fileToUpload.html");

      await blobClient.UploadAsync(fileStream,
        new BlobHttpHeaders { ContentType = "text/html" });

      return blobClient;
    }

    private static async Task SetBlobPropertiesAsync(BlobClient blobClient)
    {
      Console.WriteLine($"3. Set blob properties");

      BlobProperties blobProperties = await blobClient.GetPropertiesAsync();

      BlobHttpHeaders blobHttpHeaders = new BlobHttpHeaders
      {
        ContentType = "text/html",
        ContentLanguage = "en-us",

        CacheControl = blobProperties.CacheControl,
        ContentDisposition = blobProperties.ContentDisposition,
        ContentEncoding = blobProperties.ContentEncoding,
        ContentHash = blobProperties.ContentHash
      };

      await blobClient.SetHttpHeadersAsync(blobHttpHeaders);
    }

    private static async Task GetBlobPropertiesAsync(BlobClient blobClient)
    {
      Console.WriteLine($"4. Get blob properties");

      BlobProperties blobProperties = await blobClient.GetPropertiesAsync();

      // Display just a few of the many blob properties
      Console.WriteLine($"   - ContentType: {blobProperties.ContentType}");
      Console.WriteLine($"   - Blob type: {blobProperties.BlobType}");
      Console.WriteLine($"   - CreatedOn: {blobProperties.CreatedOn}");
      Console.WriteLine($"   - LastModified: {blobProperties.LastModified}");
    }

    private static async Task SetBlobMetadataAsync(BlobClient blobClient)
    {
      Console.WriteLine($"5. Set blob metadata");

      IDictionary<string, string> metadata = new Dictionary<string, string>();

      metadata.Add("category", "author profile");
      metadata.Add("fullname", "Thomas Claudius Huber");

      await blobClient.SetMetadataAsync(metadata);
    }

    private static async Task GetBlobMetadataAsync(BlobClient blobClient)
    {
      Console.WriteLine($"6. Get blob metadata");

      BlobProperties blobProperties = await blobClient.GetPropertiesAsync();

      foreach (var metadataItem in blobProperties.Metadata)
      {
        Console.WriteLine($"   - {metadataItem.Key} : {metadataItem.Value}");
      }
    }

    private static async Task DeleteContainerAsync()
    {
      Console.WriteLine($"7. Deleting blob container '{_blobContainerName}'");

      BlobContainerClient blobContainerClient =
          new BlobContainerClient(_connectionString, _blobContainerName);

      await blobContainerClient.DeleteIfExistsAsync();
    }
  }
}
