
"""
Example: Running Ultimate Agent with Web4ai Integration
"""

import asyncio
import logging
from ultimate_agent_bridge import UltimateWeb4aiNode

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    """Example of Ultimate Agent + Web4ai integration"""
    
    # This would normally import your actual Ultimate Agent
    # from ultimate_agent.core.agent import UltimatePainNetworkAgent
    
    # For demo, create a mock Ultimate Agent
    class MockUltimateAgent:
        def __init__(self):
            self.version = "3.0.0"
            self.agent_type = "ultimate_pain_network"
            self.config_manager = self._create_mock_config()
            self.ai_manager = self._create_mock_ai_manager()
            self.blockchain_manager = self._create_mock_blockchain_manager()
            self.security_manager = self._create_mock_security_manager()
            self.task_scheduler = self._create_mock_task_scheduler()
        
        def _create_mock_config(self):
            class MockConfig:
                def getboolean(self, section, key, fallback=False):
                    return True
                def getint(self, section, key, fallback=0):
                    return 30
            return MockConfig()
        
        def _create_mock_ai_manager(self):
            class MockAI:
                def __init__(self):
                    self.models = {'sentiment': {}, 'classification': {}}
                    self.gpu_available = True
                async def run_inference(self, model, input_data):
                    return {'prediction': 'positive', 'confidence': 0.95}
            return MockAI()
        
        def _create_mock_blockchain_manager(self):
            class MockBlockchain:
                def get_balance(self):
                    return {'PAIN': 150.0, 'ETH': 0.05}
                def execute_smart_contract(self, contract_type, method, params):
                    return {'success': True, 'result': 'executed'}
                def send_earnings(self, amount, task_id, currency='PAIN'):
                    return f"tx_{task_id}"
            return MockBlockchain()
        
        def _create_mock_security_manager(self):
            class MockSecurity:
                def generate_auth_token(self, agent_id, permissions):
                    return f"token_{agent_id}"
                def validate_auth_token(self, token, permission=None):
                    return {'valid': True, 'agent_id': 'test'}
                def get_security_status(self):
                    return {'active_tokens': 5, 'security_events': 10}
            return MockSecurity()
        
        def _create_mock_task_scheduler(self):
            class MockTaskScheduler:
                def __init__(self):
                    self.tasks = {}
                async def start_task(self, task_type, config):
                    task_id = f"task_{len(self.tasks)}"
                    self.tasks[task_id] = {'status': 'running', 'type': task_type}
                    return task_id
                def get_task_status(self, task_id):
                    if task_id in self.tasks:
                        return {'completed': True, 'result': 'success', 'duration': 5.2}
                    return None
            return MockTaskScheduler()
    
    # Create Ultimate Agent
    ultimate_agent = MockUltimateAgent()
    
    # Create Web4ai configuration
    web4ai_config = {
        'node_id': 'ultimate-demo-node',
        'listen_port': 9001,
        'agent_name': 'ultimate-demo'
    }
    
    # Create Ultimate Web4ai node
    node = UltimateWeb4aiNode(web4ai_config, ultimate_agent)
    
    try:
        # Start the integrated node
        await node.start()
        logger.info("✅ Ultimate Agent + Web4ai integration started")
        
        # Wait for network stabilization
        await asyncio.sleep(3)
        
        # Example 1: Submit Ultimate Agent task to Web4ai network
        logger.info("📋 Testing task submission...")
        task_config = {
            'type': 'ai_training',
            'config': {
                'model': 'transformer',
                'epochs': 5,
                'dataset': 'sentiment_data'
            },
            'priority': 8,
            'timeout': 300
        }
        
        task_id = await node.submit_ultimate_task(task_config)
        logger.info(f"✅ Task submitted: {task_id}")
        
        # Example 2: Distributed inference
        logger.info("🧠 Testing distributed inference...")
        inference_result = await node.distributed_inference(
            'sentiment',
            "Ultimate Agent + Web4ai integration is revolutionary!",
            priority=7,
            timeout=20.0
        )
        logger.info(f"🔮 Inference result: {inference_result}")
        
        # Example 3: Smart contract execution
        logger.info("⛓️ Testing smart contract execution...")
        contract_result = await node.execute_smart_contract(
            'task_rewards',
            'claimReward',
            {'amount': 5.0, 'task_id': task_id}
        )
        logger.info(f"💰 Contract result: {contract_result}")
        
        # Example 4: Token management
        logger.info("🪙 Testing token claiming...")
        claimed_tokens = await node.claim_pain_tokens()
        logger.info(f"💎 Claimed tokens: {claimed_tokens} PAIN")
        
        # Monitor status
        for i in range(10):
            status = node.get_ultimate_status()
            logger.info(f"📊 Status update {i+1}:")
            logger.info(f"   Domain: {status.get('ultimate_domain')}")
            logger.info(f"   Components: {status.get('components', {})}")
            logger.info(f"   Tokens: {status.get('token_status', {})}")
            await asyncio.sleep(2)
        
        logger.info("🎉 Ultimate Agent + Web4ai integration test completed!")
        
    except Exception as e:
        logger.error(f"❌ Integration test failed: {e}")
        raise
    finally:
        await node.stop()
        logger.info("🛑 Ultimate Agent + Web4ai node stopped")

if __name__ == "__main__":
    asyncio.run(main())