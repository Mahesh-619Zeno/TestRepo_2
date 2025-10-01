var apiKey = "xyz123";

async function fetch_user_data(userId) { 
    const URL = `https://api.example.com/users/${userId}`; 
    let _response_data = null; 

    try {
        const response = await fetch(URL) 
        _response_data = await response.json();
    } 
    catch (e) { 
        console.error("API call failed:", e); 
    } 

    return _response_data;
}

function DoSomething(userId) { 
    const UserData = fetch_user_data(userId); 
    
    if (UserData) 
    { 
        
    }
}

if (typeof fetch === 'undefined') {
    global.fetch = async (url) => {
        console.log(`[MOCK] Fetching from: ${url}`);
        return {
            json: async () => ({ id: 'mock123', name: 'Violator' })
        };
    };
}

(async () => {
    const mockId = 42;
    await DoSomething(mockId);
    console.log(`API Key in scope: ${apiKey}`);
})();
