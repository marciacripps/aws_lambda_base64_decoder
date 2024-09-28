<template>
  <div class="min-h-screen w-full bg-gradient-to-r from-gray-900 via-gray-800 to-gray-900 flex flex-col items-center justify-center py-12">
    <!-- Title and Description -->
    <div class="text-center text-white mb-8 px-4">
      <h2 class="text-4xl font-extrabold mb-4">Do you have to deal with Base64 format?</h2>
      <p class="text-lg mb-2">Use my super handy online tool to decode your data.</p>
      <p class="text-lg font-semibold">Decode from Base64 format</p>
      <p class="text-md">Simply enter your data like "SGVsbG8gV29ybGQ=" and then push the decode button.</p>
    </div>

    <!-- Form -->
    <form @submit.prevent="decodeBase64" class="bg-white p-8 rounded-lg shadow-xl max-w-2xl w-full">
      <!-- Input field -->
      <textarea
        v-model="base64Data"
        rows="8"
        placeholder="Type or Paste Your Base64 Here"
        class="border border-gray-300 p-4 w-full rounded-lg mb-6 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
      ></textarea>

      <!-- Submit button -->
      <button
        type="submit"
        class="w-full bg-blue-600 text-white py-3 rounded-lg font-semibold text-lg hover:bg-blue-700 transition duration-300"
      >
        Decode
      </button>
    </form>

    <!-- Decoded Data -->
    <div v-if="decodedData" class="mt-8 bg-white p-6 rounded-lg shadow-lg max-w-2xl w-full">
      <h2 class="text-2xl font-semibold mb-4 text-blue-600">Decoded Data:</h2>
      <pre class="bg-gray-100 p-6 rounded-lg text-gray-800 overflow-auto">{{ decodedData }}</pre>
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
      if (!this.base64Data) {
        this.decodedData = "Please enter a Base64 encoded string.";
        return;
      }

      const apiUrl = import.meta.env.VITE_API_URL;

      try {
        const response = await fetch(apiUrl, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ base64: this.base64Data }),
        });

        if (!response.ok) {
          const errorData = await response.text();
          this.decodedData = `Error: ${response.statusText} - ${errorData}`;
          return;
        }

        const responseData = await response.json();
        this.decodedData = responseData.decoded || "Error: No decoded data found.";
      } catch (error) {
        this.decodedData = `Error: ${error.message}`;
      }
    },
  },
};
</script>

<style>
html, body {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
}
</style>
