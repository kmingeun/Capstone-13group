document.addEventListener('DOMContentLoaded', () => {
    fetch('/home/api/get_user_info')  // 현재 로그인된 사용자 정보를 가져옴
        .then(response => response.json())
        .then(data => {
            if (data.web_id) {
                addChargeEventListeners(data.web_id); // web_id를 사용하여 충전 이벤트 리스너 추가
                updateCreditInfo(data.web_id); // 로그인된 사용자의 크레딧 정보 업데이트
                addSubscriptionEventListeners(data.web_id); // 로그인된 사용자의 구독 정보 업데이트
                fetchSubscriptionInfo(data.web_id); // 로그인된 사용자의 구독정보 업데이트 
            } 
        })
});

// 크레딧 정보를 업데이트하는 함수
function updateCreditInfo(webId) {
    fetch(`/home/api/get_credit?web_id=${webId}`)
        .then(response => response.json())
        .then(data => {
            if (data.credit !== undefined) {
                document.getElementById('credit-amount').textContent = data.credit;
            }
        });
}

// 충전 버튼에 이벤트 리스너 추가하는 함수
function addChargeEventListeners(webId) {
    document.querySelectorAll('.charge-button').forEach(button => {
        button.addEventListener('click', () => {
            const creditToAdd = button.getAttribute('data-credit');
            chargeCredit(webId, creditToAdd);
        });
    });
}

// 크레딧을 충전하는 함수
function chargeCredit(webId, creditToAdd) {
    fetch(`/home/api/charge_credit`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ web_id: webId, credit: creditToAdd })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            updateCreditInfo(webId);  // 크레딧 정보를 다시 업데이트
            alert('크레딧 충전이 완료되었습니다!');
        } 
    })
}

// 구독 버튼에 이벤트 리스너 추가하는 함수
function addSubscriptionEventListeners(webId) {
    document.querySelectorAll('.sub_button').forEach(button => {
        button.addEventListener('click', () => {
            const subscriptionType = button.getAttribute('data-subscription');
            updateSubscriptionInfo(webId, subscriptionType);
        });
    });
}

// 구독 정보를 업데이트하는 함수
function updateSubscriptionInfo(webId, subscriptionType) {
    fetch(`/home/api/update_subscription`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ web_id: webId, subscription: subscriptionType })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('구독 정보가 업데이트되었습니다!');
            fetchSubscriptionInfo(webId);  // 구독 정보를 다시 가져와서 업데이트
        } else {
            alert('구독 정보 업데이트에 실패했습니다.');
        }
    });
}

// 구독 정보 표시 함수 
function fetchSubscriptionInfo(webId) {
    fetch(`/home/api/get_subscription?web_id=${webId}`)
        .then(response => response.json())
        .then(data => {
            const subscriptionInfoElement = document.getElementById('subscription-amount');
            if (data.subscription) {
                subscriptionInfoElement.textContent = `${data.subscription} 구독중`;
            } else {
                subscriptionInfoElement.textContent = '';
            }
        });
}
