export async function getDailyPrediction() {
    try{
        const response = await fetch('http://127.0.0.1:5000/api/daily-prediction', { mode: 'cors' });
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

export async function getDailyNews() {
    try {
        const response = await fetch('http://127.0.0.1:5000/api/daily-news', {mode: 'cors'});
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