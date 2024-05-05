export async function getDailyPrediction() {
    try{
        console.log("fetching");
        const response = await fetch('http://127.0.0.1:5000/api/daily-prediction', { mode: 'cors' });
        if (!response.ok) {
            throw new Error('Failed to fetch daily predictions');
        }

        const data = await response.json();
        console.log(data);
        console.log("good");
        return data;

    } catch (error) {
        console.error('Error:', error);
        return 'Error fetching prediction';
    }
}

export async function getTrendGraph() {
    try {
        console.log("fetching");
        const response = await fetch('http://127.0.0.1:5000/api/daily-stock', {mode: 'cors'});
        if (!response.ok) {
            throw new Error('Failed to fetch daily stock data');
        }

        const data = await response.json();
        console.log(data);
        console.log("good");
        return data;
    } catch (error) {
        console.error('Error:', error);
        return 'Error fetching graph data';
    }
}