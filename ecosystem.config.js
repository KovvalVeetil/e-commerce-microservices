module.exports = {
    apps: [
      {
        name: 'user-service',
        script: 'user_service.py',
        interpreter: 'python'
      },
      {
        name: 'product-service',
        script: 'product_service.py',
        interpreter: 'python'
      },
      {
        name: 'order-service',
        script: 'order_service.py',
        interpreter: 'python'
      },
      {
        name: 'payment-service',
        script: 'payment_service.py',
        interpreter: 'python'
      },
      {
        name: 'shipping-service',
        script: 'shipping_service.py',
        interpreter: 'python'
      },
      {
        name: 'notification-service',
        script: 'notification_service.py',
        interpreter: 'python'
      }
    ]
  };
  