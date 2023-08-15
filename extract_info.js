const { Configuration, OpenAIApi } = require("openai");
require('dotenv').config()

const configuration = new Configuration({
  apiKey: process.env.OPENAI_API_KEY,
});
const openai = new OpenAIApi(configuration);
const user_input = "I'm John Smith, and I live at 123 Main St, New York. I'm 25 years old, and you can reach me at john@example.com. My goal with this program is to improve my coding skills.";

async function runCompletion () {
    const completion = await openai.createCompletion({
    model: "text-davinci-003",
    prompt: `Extract the following information in JSON format:\nName, Location, Address, Age, Areas of interest, Goals.\nIf any data is missing, set it as None.\n\n${user_input}`,
    max_tokens:100
    });
    console.log(completion.data.choices[0].text);
}

runCompletion();