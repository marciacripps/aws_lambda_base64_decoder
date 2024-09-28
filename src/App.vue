<template>
  <div class="min-h-screen bg-gray-100 flex flex-col items-center justify-center">
    <!-- Title -->
    <h1 class="text-3xl font-bold text-blue-600 mb-8">Base64 Decoder</h1>

    <!-- Form -->
    <form @submit.prevent="decodeBase64" class="bg-white p-6 rounded shadow-lg max-w-lg w-full">
      <!-- Input field -->
      <input
        v-model="base64Data"
        type="text"
        placeholder="Enter Base64"
        class="border border-gray-300 p-3 w-full rounded mb-4"
      />

      <!-- Submit button -->
      <button
        type="submit"
        class="bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-700 w-full"
      >
        Decode
      </button>
    </form>

    <!-- Decoded Data -->
    <div v-if="decodedData" class="mt-8 bg-white p-6 rounded shadow-lg max-w-lg w-full">
      <h2 class="text-xl font-semibold mb-2">Decoded Data:</h2>
      <p class="bg-blue-50 p-4 rounded text-black">{{ decodedData }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      base64Data: "", // Stores the input from the user
      decodedData: null, // Will store the decoded data from the API response
    };
  },
  methods: {
    async decodeBase64() {
      console.log("Input Base64 data:", this.base64Data);

      if (!this.base64Data) {
        console.warn("No Base64 data entered.");
        this.decodedData = "Please enter a Base64 encoded string.";
        return;
      }

      // Access the API URL from the .env file using import.meta.env.VITE_API_URL
      const apiUrl = import.meta.env.VITE_API_URL;
      console.log("Sending request to:", apiUrl);

      try {
        const response = await fetch(apiUrl, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ base64: this.base64Data }),  // Sending the Base64 data
        });

        console.log("Raw response from API Gateway:", response);

        if (!response.ok) {
          const errorData = await response.text();  // Log the error response body for further insight
          console.error("Failed to fetch:", response.statusText, errorData);
          this.decodedData = `Error: ${response.statusText} - ${errorData}`;
          return;
        }

        const responseData = await response.json();
        console.log("Parsed response data:", responseData);

        if (responseData.decoded) {
          this.decodedData = responseData.decoded;
        } else {
          console.warn("No decoded data found in the response.");
          this.decodedData = "Error: No decoded data found.";
        }

      } catch (error) {
        console.error("Error during fetch:", error);
        this.decodedData = `Error: ${error.message}`;
      }
    },
  },
};
</script>

<style>

</style>
