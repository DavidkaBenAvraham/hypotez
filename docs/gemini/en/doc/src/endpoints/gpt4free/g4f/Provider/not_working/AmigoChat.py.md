# AmigoChat Provider

## Overview

This module provides the `AmigoChat` class, which acts as a provider for interacting with the AmigoChat.io API. It allows for asynchronous generation of text and images using various language models. 

The `AmigoChat` class inherits from `AsyncGeneratorProvider` and `ProviderModelMixin`, providing functionality for asynchronous stream-based responses and managing model selection. The module utilizes `StreamSession` for handling HTTP requests and `raise_for_status` for error handling.

## Details

The `AmigoChat` class utilizes the AmigoChat.io API for generating responses based on user input. It supports both chat and image generation tasks with a wide range of language models. 

The module provides a comprehensive set of features including:

- **Model Aliases:**  Provides alias names for common models for simplified usage.
- **Chat and Image Generation:**  Handles both text and image generation requests.
- **Stream Support:** Enables stream-based responses for real-time feedback.
- **System Messages:** Allows for the inclusion of system messages to influence the model's behavior.
- **Message History:** Supports the use of message history for context-aware responses.

## Classes

### `class AmigoChat`

**Description:** The `AmigoChat` class is a provider for interacting with the AmigoChat.io API for generating text and images using various language models.

**Inherits:** 
- `AsyncGeneratorProvider`: Provides functionality for creating asynchronous generators for stream-based responses.
- `ProviderModelMixin`: Provides utility methods for managing model selection and aliasing.

**Attributes:**

- `url (str)`: The base URL of the AmigoChat.io API.
- `chat_api_endpoint (str)`: The endpoint for chat completions.
- `image_api_endpoint (str)`: The endpoint for image generations.
- `working (bool)`: Indicates whether the provider is currently operational.
- `supports_stream (bool)`: Indicates support for stream-based responses.
- `supports_system_message (bool)`: Indicates support for system messages.
- `supports_message_history (bool)`: Indicates support for message history.
- `default_model (str)`: The default model to use for generation tasks.
- `chat_models (list)`: A list of available chat models.
- `image_models (list)`: A list of available image models.
- `models (list)`: A combined list of chat and image models.
- `model_aliases (dict)`: A dictionary mapping model aliases to their corresponding model names.

**Methods:**

#### `get_personaId(model: str) -> str`

**Purpose:** Retrieves the persona ID for a given model.

**Parameters:**

- `model (str)`: The model name.

**Returns:**

- `str`: The persona ID corresponding to the specified model.

**Raises Exceptions:**

- `ValueError`: If the provided model is not recognized.

#### `generate_chat_id() -> str`

**Purpose:** Generates a unique chat ID in the format of an 8-4-4-4-12 hexadecimal string.

**Returns:**

- `str`: The generated chat ID.

#### `create_async_generator(model: str, messages: Messages, proxy: str = None, stream: bool = False, timeout: int = 300, frequency_penalty: float = 0, max_tokens: int = 4000, presence_penalty: float = 0, temperature: float = 0.5, top_p: float = 0.95, **kwargs) -> AsyncResult`

**Purpose:** Creates an asynchronous generator that yields responses from the AmigoChat.io API based on the provided parameters.

**Parameters:**

- `model (str)`: The model name.
- `messages (Messages)`: A list of messages to be used as context for the generation task.
- `proxy (str, optional)`:  A proxy server address to use for the request. Defaults to None.
- `stream (bool, optional)`: Whether to stream the response or return the complete response. Defaults to False.
- `timeout (int, optional)`: The maximum time in seconds to wait for a response. Defaults to 300.
- `frequency_penalty (float, optional)`: A penalty applied to tokens that have already appeared in the text. Defaults to 0.
- `max_tokens (int, optional)`: The maximum number of tokens to generate. Defaults to 4000.
- `presence_penalty (float, optional)`: A penalty applied to tokens that have already appeared in the text. Defaults to 0.
- `temperature (float, optional)`:  The temperature parameter controls the randomness of the generated text. Defaults to 0.5.
- `top_p (float, optional)`: The top_p parameter controls the diversity of the generated text. Defaults to 0.95.
- `**kwargs`: Additional keyword arguments to be passed to the request.

**Returns:**

- `AsyncResult`: An asynchronous result object representing the generation task.

**Raises Exceptions:**

- `ResponseStatusError`: If the response from the server indicates an error.
- `Exception`: If an error occurs during the request.

## Example File

```python
from __future__ import annotations

import json
import uuid

from ...typing import AsyncResult, Messages
from ..base_provider import AsyncGeneratorProvider, ProviderModelMixin
from ...providers.response import ImageResponse
from ...requests import StreamSession, raise_for_status
from ...errors import ResponseStatusError

MODELS = {
    'chat': {
        'gpt-4o-2024-11-20': {'persona_id': "gpt"},
        'gpt-4o': {'persona_id': "summarizer"},
        'gpt-4o-mini': {'persona_id': "amigo"},

        'o1-preview-': {'persona_id': "openai-o-one"}, # Amigo, your balance is not enough to make the request, wait until 12 UTC or upgrade your plan
        'o1-preview-2024-09-12-': {'persona_id': "orion"}, # Amigo, your balance is not enough to make the request, wait until 12 UTC or upgrade your plan
        'o1-mini-': {'persona_id': "openai-o-one-mini"}, # Amigo, your balance is not enough to make the request, wait until 12 UTC or upgrade your plan
        
        'meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo': {'persona_id': "llama-three-point-one"},
        'meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo': {'persona_id': "llama-3-2"},
        'codellama/CodeLlama-34b-Instruct-hf': {'persona_id': "codellama-CodeLlama-34b-Instruct-hf"},
        
        'gemini-1.5-pro': {'persona_id': "gemini-1-5-pro"}, # Amigo, your balance is not enough to make the request, wait until 12 UTC or upgrade your plan
        'gemini-1.5-flash': {'persona_id': "gemini-1.5-flash"},
        
        'claude-3-5-sonnet-20240620': {'persona_id': "claude"},
        'claude-3-5-sonnet-20241022': {'persona_id': "clude-claude-3-5-sonnet-20241022"},
        'claude-3-5-haiku-latest': {'persona_id': "3-5-haiku"},
        
        'Qwen/Qwen2.5-72B-Instruct-Turbo': {'persona_id': "qwen-2-5"},
        
        'google/gemma-2b-it': {'persona_id': "google-gemma-2b-it"},
        'google/gemma-7b': {'persona_id': "google-gemma-7b"}, # Error handling AIML chat completion stream
        
        'Gryphe/MythoMax-L2-13b': {'persona_id': "Gryphe-MythoMax-L2-13b"},
        
        'mistralai/Mistral-7B-Instruct-v0.3': {'persona_id': "mistralai-Mistral-7B-Instruct-v0.1"},
        'mistralai/mistral-tiny': {'persona_id': "mistralai-mistral-tiny"},
        'mistralai/mistral-nemo': {'persona_id': "mistralai-mistral-nemo"},
        
        'deepseek-ai/deepseek-llm-67b-chat': {'persona_id': "deepseek-ai-deepseek-llm-67b-chat"},
        
        'databricks/dbrx-instruct': {'persona_id': "databricks-dbrx-instruct"},
        
        'NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO': {'persona_id': "NousResearch-Nous-Hermes-2-Mixtral-8x7B-DPO"},
        
        'x-ai/grok-beta': {'persona_id': "x-ai-grok-beta"},
        
        'anthracite-org/magnum-v4-72b': {'persona_id': "anthracite-org-magnum-v4-72b"},
        
        'cohere/command-r-plus': {'persona_id': "cohere-command-r-plus"},
        
        'ai21/jamba-1-5-mini': {'persona_id': "ai21-jamba-1-5-mini"},
        
        'zero-one-ai/Yi-34B': {'persona_id': "zero-one-ai-Yi-34B"} # Error handling AIML chat completion stream
    },
    
    'image': {
        'flux-pro/v1.1': {'persona_id': "flux-1-1-pro"}, # Amigo, your balance is not enough to make the request, wait until 12 UTC or upgrade your plan
        'flux-realism': {'persona_id': "flux-realism"},
        'flux-pro': {'persona_id': "flux-pro"}, # Amigo, your balance is not enough to make the request, wait until 12 UTC or upgrade your plan
        'flux-pro/v1.1-ultra': {'persona_id': "flux-pro-v1.1-ultra"}, # Amigo, your balance is not enough to make the request, wait until 12 UTC or upgrade your plan
        'flux-pro/v1.1-ultra-raw': {'persona_id': "flux-pro-v1.1-ultra-raw"}, # Amigo, your balance is not enough to make the request, wait until 12 UTC or upgrade your plan
        'flux/dev': {'persona_id': "flux-dev"},

        'dall-e-3': {'persona_id': "dalle-three"},

        'recraft-v3': {'persona_id': "recraft"}
    }
}

class AmigoChat(AsyncGeneratorProvider, ProviderModelMixin):
    url = "https://amigochat.io/chat/"
    chat_api_endpoint = "https://api.amigochat.io/v1/chat/completions"
    image_api_endpoint = "https://api.amigochat.io/v1/images/generations"
    
    working = False
    supports_stream = True
    supports_system_message = True
    supports_message_history = True
       
    default_model = 'gpt-4o-mini'

    chat_models = list(MODELS['chat'].keys())
    image_models = list(MODELS['image'].keys())
    models = chat_models + image_models
    
    model_aliases = {
        ### chat ###
        "gpt-4o": "gpt-4o-2024-11-20",
        "gpt-4o-mini": "gpt-4o-mini",
        
        "llama-3.1-405b": "meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo",
        "llama-3.2-90b": "meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo",
        "codellama-34b": "codellama/CodeLlama-34b-Instruct-hf",
        
        "gemini-flash": "gemini-1.5-flash",
        
        "claude-3.5-sonnet": "claude-3-5-sonnet-20240620",
        "claude-3.5-sonnet": "claude-3-5-sonnet-20241022",
        "claude-3.5-haiku": "claude-3-5-haiku-latest",
        
        "qwen-2.5-72b": "Qwen/Qwen2.5-72B-Instruct-Turbo",
        "gemma-2b": "google/gemma-2b-it",
        
        "mythomax-13b": "Gryphe/MythoMax-L2-13b",
        
        "mixtral-7b": "mistralai/Mistral-7B-Instruct-v0.3",
        "mistral-nemo": "mistralai/mistral-nemo",
        
        "deepseek-chat": "deepseek-ai/deepseek-llm-67b-chat",
        
        "dbrx-instruct": "databricks/dbrx-instruct",
        
        "mixtral-8x7b-dpo": "NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO",
        
        "grok-beta": "x-ai/grok-beta",
        
        "magnum-72b": "anthracite-org/magnum-v4-72b",
        
        "command-r-plus": "cohere/command-r-plus",
        
        "jamba-mini": "ai21/jamba-1-5-mini",
        
        
        ### image ###
        "flux-dev": "flux/dev",
    }

    @classmethod
    def get_personaId(cls, model: str) -> str:
        if model in cls.chat_models:
            return MODELS['chat'][model]['persona_id']
        elif model in cls.image_models:
            return MODELS['image'][model]['persona_id']
        else:
            raise ValueError(f"Unknown model: {model}")
            
    @staticmethod
    def generate_chat_id() -> str:
        """Generate a chat ID in format: 8-4-4-4-12 hexadecimal digits"""
        return str(uuid.uuid4())
	
    @classmethod
    async def create_async_generator(
        cls,
        model: str,
        messages: Messages,
        proxy: str = None,
        stream: bool = False,
        timeout: int = 300,
        frequency_penalty: float = 0,
        max_tokens: int = 4000,
        presence_penalty: float = 0,
        temperature: float = 0.5,
        top_p: float = 0.95,
        **kwargs
    ) -> AsyncResult:
        model = cls.get_model(model)
        
        device_uuid = str(uuid.uuid4())
        max_retries = 3
        retry_count = 0

        while retry_count < max_retries:
            try:
                headers = {
                    "accept": "*/*",
                    "accept-language": "en-US,en;q=0.9",
                    "authorization": "Bearer",
                    "cache-control": "no-cache",
                    "content-type": "application/json",
                    "origin": cls.url,
                    "pragma": "no-cache",
                    "priority": "u=1, i",
                    "referer": f"{cls.url}/",
                    "sec-ch-ua": '"Chromium";v="129", "Not=A?Brand";v="8"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": '"Linux"',
                    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
                    "x-device-language": "en-US",
                    "x-device-platform": "web",
                    "x-device-uuid": device_uuid,
                    "x-device-version": "1.0.45"
                }
                
                async with StreamSession(headers=headers, proxy=proxy) as session:
                    if model not in cls.image_models:
                        data = {
                            "chatId": cls.generate_chat_id(),
                            "frequency_penalty": frequency_penalty,
                            "max_tokens": max_tokens,
                            "messages": messages,
                            "model": model,
                            "personaId": cls.get_personaId(model),
                            "presence_penalty": presence_penalty,
                            "stream": stream,
                            "temperature": temperature,
                            "top_p": top_p
                        }
                        async with session.post(cls.chat_api_endpoint, json=data, timeout=timeout) as response:
                            await raise_for_status(response)
                            async for line in response.iter_lines():
                                line = line.decode('utf-8').strip()
                                if line.startswith('data: '):
                                    if line == 'data: [DONE]':
                                        break
                                    try:
                                        chunk = json.loads(line[6:])  # Remove 'data: ' prefix
                                        if 'choices' in chunk and len(chunk['choices']) > 0:
                                            choice = chunk['choices'][0]
                                            if 'delta' in choice:
                                                content = choice['delta'].get('content')
                                            elif 'text' in choice:
                                                content = choice['text']
                                            else:
                                                content = None
                                            if content:
                                                yield content
                                    except json.JSONDecodeError:
                                        pass
                    else:
                        # Image generation
                        prompt = messages[-1]['content']
                        data = {
                            "prompt": prompt,
                            "model": model,
                            "personaId": cls.get_personaId(model)
                        }
                        async with session.post(cls.image_api_endpoint, json=data) as response:
                            await raise_for_status(response)
                            response_data = await response.json()
                            if "data" in response_data:
                                image_urls = []
                                for item in response_data["data"]:
                                    if "url" in item:
                                        image_url = item["url"]
                                        image_urls.append(image_url)
                                if image_urls:
                                    yield ImageResponse(image_urls, prompt)
                            else:
                                yield None
                break
            except (ResponseStatusError, Exception) as e:
                retry_count += 1
                if retry_count >= max_retries:
                    raise e
                device_uuid = str(uuid.uuid4())

                ```