export async function getPredictionOnDate(date = new Date().toISOString().split('T')[0] ){
    try{
        const response = await fetch(`http://127.0.0.1:5000/api/daily-prediction?date=${date}`, { mode: 'cors' });
        if (!response.ok) {
            throw new Error('Failed to fetch daily predictions');
        }

        const data = await response.json();
        return data;

    } catch (error) {
        console.error('Error:', error);
        return error;
    }
}

export async function getTrendGraph(timeFrame, type) {
    try {
        const response = await fetch(`http://127.0.0.1:5000/api/daily-stock?timeFrame=${timeFrame}&type=${type}`, {mode: 'cors'});
        if (!response.ok) {
            throw new Error('Failed to fetch daily stock dataload');
        }

        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error:', error);
        return error;
    }
}

export async function getStat(timeFrame, type) {
    try {
        const response = await fetch(`http://127.0.0.1:5000/api/daily-stats?timeFrame=${timeFrame}&type=${type}`, {mode: 'cors'});
        if (!response.ok) {
            const text = await response.text();
            throw new Error(`Failed to fetch daily stats, status: ${response.status}, body: ${text}`);
        }

        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error:', error);
        return error;
    }
}

export async function getDailyPrice() {
    try {
        const response = await fetch('http://127.0.0.1:5000/api/daily-price', {mode: 'cors'});
        if (!response.ok) {
            throw new Error('Failed to fetch daily price');
        }

        const data = await response.json();
        return data;
    }
    catch (error) {
        console.error('Error:', error);
        return error;
    }
}

export async function getDailyNews(date = new Date().toISOString().split('T')[0] ) {
    try {
        const response = await fetch(`http://127.0.0.1:5000/api/daily-news?date=${date}`, {mode: 'cors'});
        if (!response.ok) {
            throw new Error('Failed to fetch daily news');
        }

        const data = await response.json();
        return data;
    }
    catch (error) {
        console.error('Error:', error);
        return error;
    }
}

export async function getSearchResults(query) {
    try {
        const response = await fetch(`http://127.0.0.1:5000/api/search?query=${query}`, {mode: 'cors'});
        if (!response.ok) {
            throw new Error('Failed to fetch search results');
        }

        let data = await response.json();
        const titles = data.map((item) => item.title);
        return titles.slice(0, 1);
    } catch (error) {
        console.error('Error:', error);
        return error;
    }
}

export async function getSpecificStockInfo(ticker) {
    try {
        const response = await fetch(`http://127.0.0.1:5000/api/specific-stock-info?ticker=${ticker}`, {mode: 'cors'});
        if (!response.ok) {
            throw new Error('Failed to fetch specific stock info');
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error:', error);
        return error;
    }
}

export async function getSpecialGraph(ticker) {
    try {
        const response = await fetch(`http://127.0.0.1:5000/api/spec-graph?ticker=${ticker}`, {mode: 'cors'});
        if (!response.ok) {
            throw new Error('Failed to fetch special graph');
        }

        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error:', error);
        return error;
    }
}