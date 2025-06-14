
"""
Enhanced Web4ai Bridge for Ultimate Agent
Integrates Web4ai mesh with Ultimate Agent's advanced P2P and blockchain systems
"""

import asyncio
import time
import json
import uuid
import logging
from typing import Dict, Any, Optional, List
from dataclasses import dataclass, asdict

# Import Web4ai base components
from ..enhanced_network.core.mesh_node import MeshNode, NetworkMessage

# Import Ultimate Agent components (adjust paths as needed)
from ultimate_agent.network.p2p.distributed_ai import (
    P2PNetworkManager, P2PDistributedAIIntegration, 
    NodeType, MessageType, InferenceTask, NodeCapability
)
from ultimate_agent.blockchain.wallet.security import BlockchainManager
from ultimate_agent.security.authentication import SecurityManager

@dataclass
class UltimateAgentCapability:
    """Enhanced capability description for Ultimate Agent"""
    node_id: str
    agent_type: str
    web4ai_domain: str
    p2p_capabilities: NodeCapability
    security_level: str
    blockchain_enabled: bool
    models_available: List[str]
    compute_resources: Dict[str, Any]
    reputation_score: float
    pain_token_balance: float

class UltimateAgentWeb4aiBridge:
    """Advanced bridge between Web4ai and Ultimate Agent systems"""
    
    def __init__(self, web4ai_node: MeshNode, ultimate_agent):
        self.web4ai_node = web4ai_node
        self.ultimate_agent = ultimate_agent
        self.logger = logging.getLogger(f"UltimateWeb4aiBridge-{web4ai_node.node_id}")
        
        # Get Ultimate Agent managers
        self.ai_manager = getattr(ultimate_agent, 'ai_manager', None)
        self.blockchain_manager = getattr(ultimate_agent, 'blockchain_manager', None)
        self.security_manager = getattr(ultimate_agent, 'security_manager', None)
        self.task_scheduler = getattr(ultimate_agent, 'task_scheduler', None)
        
        # Initialize P2P integration if available
        self.p2p_integration = None
        if hasattr(ultimate_agent, 'config_manager'):
            self._init_p2p_integration()
        
        # Token management
        self.token_manager = TokenManager(self)
        self.governance = GovernanceManager(self)
        
        # Domain and identity
        self.web4ai_domain = f"{web4ai_node.node_id}.pain.web4ai"
        self.ultimate_capability = self._create_capability_profile()
        
        # Register enhanced message handlers
        self._register_ultimate_handlers()
        
        self.logger.info("Ultimate Agent Web4ai Bridge initialized")
    
    def _init_p2p_integration(self):
        """Initialize P2P integration with Ultimate Agent's system"""
        try:
            if (hasattr(self.ultimate_agent, 'config_manager') and 
                self.ai_manager and self.blockchain_manager):
                
                self.p2p_integration = P2PDistributedAIIntegration(
                    self.ultimate_agent.config_manager,
                    self.ai_manager,
                    self.blockchain_manager
                )
                self.logger.info("P2P integration initialized")
        except Exception as e:
            self.logger.warning(f"P2P integration failed: {e}")
    
    def _create_capability_profile(self) -> UltimateAgentCapability:
        """Create comprehensive capability profile"""
        # Get P2P capabilities if available
        p2p_caps = None
        if self.p2p_integration:
            try:
                p2p_status = self.p2p_integration.get_p2p_status()
                p2p_caps = NodeCapability(
                    node_id=self.web4ai_node.node_id,
                    node_type=NodeType.FULL_NODE,
                    models=list(getattr(self.ai_manager, 'models', {}).keys()),
                    compute_power=self._estimate_compute_power(),
                    memory_gb=self._get_memory_gb(),
                    bandwidth_mbps=100.0,
                    gpu_available=getattr(self.ai_manager, 'gpu_available', False),
                    reliability_score=1.0,
                    last_seen=time.time()
                )
            except Exception as e:
                self.logger.warning(f"Failed to create P2P capabilities: {e}")
        
        # Get blockchain info
        pain_balance = 0.0
        if self.blockchain_manager:
            try:
                balances = self.blockchain_manager.get_balance()
                pain_balance = balances.get('PAIN', 0.0)
            except Exception:
                pass
        
        return UltimateAgentCapability(
            node_id=self.web4ai_node.node_id,
            agent_type=getattr(self.ultimate_agent, 'agent_type', 'ultimate_agent'),
            web4ai_domain=self.web4ai_domain,
            p2p_capabilities=p2p_caps,
            security_level='high' if self.security_manager else 'basic',
            blockchain_enabled=self.blockchain_manager is not None,
            models_available=list(getattr(self.ai_manager, 'models', {}).keys()),
            compute_resources=self._get_compute_resources(),
            reputation_score=1.0,
            pain_token_balance=pain_balance
        )
    
    def _register_ultimate_handlers(self):
        """Register Ultimate Agent specific message handlers"""
        handlers = {
            'ultimate_task_request': self._handle_ultimate_task_request,
            'ultimate_inference_request': self._handle_ultimate_inference_request,
            'ultimate_model_share': self._handle_ultimate_model_share,
            'ultimate_p2p_message': self._handle_ultimate_p2p_message,
            'ultimate_blockchain_tx': self._handle_ultimate_blockchain_tx,
            'ultimate_security_auth': self._handle_ultimate_security_auth,
            'ultimate_capability_query': self._handle_ultimate_capability_query,
            'ultimate_governance_proposal': self._handle_ultimate_governance_proposal
        }
        
        for message_type, handler in handlers.items():
            self.web4ai_node.register_message_handler(message_type, handler)
    
    async def announce_ultimate_capabilities(self):
        """Announce Ultimate Agent capabilities to Web4ai network"""
        announcement = {
            'action': 'ultimate_agent_announcement',
            'capability': asdict(self.ultimate_capability),
            'web4ai_domain': self.web4ai_domain,
            'ultimate_agent_version': getattr(self.ultimate_agent, 'version', '3.0.0'),
            'features': self._get_feature_list(),
            'timestamp': time.time()
        }
        
        await self.web4ai_node.broadcast_message('ultimate_capability_query', announcement)
        self.logger.info(f"Announced Ultimate Agent capabilities: {self.web4ai_domain}")
    
    def _get_feature_list(self) -> List[str]:
        """Get list of available Ultimate Agent features"""
        features = ['web4ai_integration', 'mesh_networking']
        
        if self.ai_manager:
            features.extend(['ai_inference', 'model_management'])
        if self.blockchain_manager:
            features.extend(['blockchain_integration', 'smart_contracts', 'multi_currency'])
        if self.security_manager:
            features.extend(['advanced_security', 'token_auth', 'encryption'])
        if self.p2p_integration:
            features.extend(['p2p_networking', 'distributed_inference', 'consensus'])
        if self.task_scheduler:
            features.extend(['task_scheduling', 'task_distribution'])
        
        return features
    
    async def _handle_ultimate_task_request(self, message: NetworkMessage):
        """Handle Ultimate Agent task requests"""
        try:
            task_data = message.payload
            
            if not self.task_scheduler:
                await self.web4ai_node.send_message(message.sender_id, 'task_response', {
                    'status': 'error',
                    'message': 'Task scheduler not available'
                })
                return
            
            # Check security if enabled
            if self.security_manager and task_data.get('auth_token'):
                validation = self.security_manager.validate_auth_token(
                    task_data['auth_token'], 
                    'execute'
                )
                if not validation['valid']:
                    await self.web4ai_node.send_message(message.sender_id, 'task_response', {
                        'status': 'error',
                        'message': 'Authentication failed'
                    })
                    return
            
            # Execute task using Ultimate Agent's task scheduler
            task_id = await self._execute_ultimate_task(task_data, message.sender_id)
            
            await self.web4ai_node.send_message(message.sender_id, 'task_response', {
                'status': 'accepted',
                'task_id': task_id,
                'agent_type': 'ultimate_agent'
            })
            
        except Exception as e:
            self.logger.error(f"Ultimate task request failed: {e}")
            await self.web4ai_node.send_message(message.sender_id, 'task_response', {
                'status': 'error',
                'message': str(e)
            })
    
    async def _handle_ultimate_inference_request(self, message: NetworkMessage):
        """Handle distributed inference requests using Ultimate Agent's P2P system"""
        try:
            request_data = message.payload
            model_name = request_data['model']
            input_data = request_data['input']
            
            if self.p2p_integration:
                # Use distributed inference
                result = await self.p2p_integration.distributed_inference(
                    model_name,
                    input_data,
                    priority=request_data.get('priority', 5),
                    timeout=request_data.get('timeout', 30.0)
                )
            elif self.ai_manager:
                # Fall back to local inference
                result = await self._local_inference(model_name, input_data)
            else:
                result = {'success': False, 'error': 'No inference capability available'}
            
            await self.web4ai_node.send_message(message.sender_id, 'inference_response', {
                'request_id': request_data.get('request_id'),
                'result': result,
                'processed_by': 'ultimate_agent'
            })
            
        except Exception as e:
            self.logger.error(f"Ultimate inference request failed: {e}")
    
    async def _handle_ultimate_blockchain_tx(self, message: NetworkMessage):
        """Handle blockchain transactions"""
        try:
            tx_data = message.payload
            
            if not self.blockchain_manager:
                await self.web4ai_node.send_message(message.sender_id, 'blockchain_response', {
                    'status': 'error',
                    'message': 'Blockchain not available'
                })
                return
            
            # Execute blockchain operation
            if tx_data['type'] == 'smart_contract':
                result = self.blockchain_manager.execute_smart_contract(
                    tx_data['contract_type'],
                    tx_data['method'],
                    tx_data['params']
                )
            elif tx_data['type'] == 'token_transfer':
                result = self.blockchain_manager.send_earnings(
                    tx_data['amount'],
                    tx_data['task_id'],
                    tx_data.get('currency', 'PAIN')
                )
            else:
                result = {'success': False, 'error': 'Unknown transaction type'}
            
            await self.web4ai_node.send_message(message.sender_id, 'blockchain_response', {
                'transaction_id': tx_data.get('tx_id'),
                'result': result
            })
            
        except Exception as e:
            self.logger.error(f"Blockchain transaction failed: {e}")
    
    async def _handle_ultimate_security_auth(self, message: NetworkMessage):
        """Handle security and authentication requests"""
        try:
            auth_data = message.payload
            
            if not self.security_manager:
                await self.web4ai_node.send_message(message.sender_id, 'auth_response', {
                    'status': 'error',
                    'message': 'Security manager not available'
                })
                return
            
            if auth_data['type'] == 'generate_token':
                token = self.security_manager.generate_auth_token(
                    auth_data['agent_id'],
                    auth_data.get('permissions', ['read', 'write'])
                )
                result = {'status': 'success', 'token': token}
            elif auth_data['type'] == 'validate_token':
                validation = self.security_manager.validate_auth_token(
                    auth_data['token'],
                    auth_data.get('required_permission')
                )
                result = {'status': 'success', 'validation': validation}
            else:
                result = {'status': 'error', 'message': 'Unknown auth type'}
            
            await self.web4ai_node.send_message(message.sender_id, 'auth_response', result)
            
        except Exception as e:
            self.logger.error(f"Security auth request failed: {e}")
    
    async def _handle_ultimate_capability_query(self, message: NetworkMessage):
        """Handle capability queries"""
        response = {
            'node_id': self.web4ai_node.node_id,
            'capability': asdict(self.ultimate_capability),
            'features': self._get_feature_list(),
            'status': self.get_ultimate_status()
        }
        
        await self.web4ai_node.send_message(message.sender_id, 'capability_response', response)
    
    async def _handle_ultimate_governance_proposal(self, message: NetworkMessage):
        """Handle governance proposals"""
        try:
            proposal_data = message.payload
            
            if proposal_data['action'] == 'create':
                proposal_id = await self.governance.create_proposal(proposal_data)
                result = {'status': 'success', 'proposal_id': proposal_id}
            elif proposal_data['action'] == 'vote':
                await self.governance.vote_on_proposal(
                    proposal_data['proposal_id'],
                    proposal_data['vote'],
                    proposal_data.get('voting_power', 1.0)
                )
                result = {'status': 'success', 'message': 'Vote recorded'}
            else:
                result = {'status': 'error', 'message': 'Unknown governance action'}
            
            await self.web4ai_node.send_message(message.sender_id, 'governance_response', result)
            
        except Exception as e:
            self.logger.error(f"Governance proposal failed: {e}")
    
    async def _execute_ultimate_task(self, task_data: Dict[str, Any], requester_id: str) -> str:
        """Execute task using Ultimate Agent's advanced capabilities"""
        task_id = f"ultimate-{uuid.uuid4().hex[:8]}"
        
        try:
            # Create task configuration
            task_config = {
                'type': task_data['type'],
                'config': task_data.get('config', {}),
                'requester': requester_id,
                'web4ai_task': True,
                'priority': task_data.get('priority', 5)
            }
            
            # Use Ultimate Agent's task scheduler
            if hasattr(self.task_scheduler, 'start_task'):
                ultimate_task_id = await self.task_scheduler.start_task(
                    task_config['type'],
                    task_config['config']
                )
                
                # Monitor task progress and send updates
                asyncio.create_task(self._monitor_task_progress(
                    ultimate_task_id, 
                    task_id, 
                    requester_id
                ))
                
            return task_id
            
        except Exception as e:
            self.logger.error(f"Task execution failed: {e}")
            raise
    
    async def _monitor_task_progress(self, ultimate_task_id: str, web4ai_task_id: str, requester_id: str):
        """Monitor Ultimate Agent task progress and send updates"""
        try:
            while True:
                # Get task status from Ultimate Agent
                if hasattr(self.task_scheduler, 'get_task_status'):
                    status = self.task_scheduler.get_task_status(ultimate_task_id)
                    
                    if status and status.get('completed'):
                        # Send completion notification
                        await self.web4ai_node.send_message(requester_id, 'task_complete', {
                            'task_id': web4ai_task_id,
                            'result': status.get('result'),
                            'execution_time': status.get('duration'),
                            'processed_by': 'ultimate_agent'
                        })
                        
                        # Award PAIN tokens for task completion
                        await self._award_task_completion_tokens(ultimate_task_id, status)
                        break
                        
                    elif status and status.get('failed'):
                        await self.web4ai_node.send_message(requester_id, 'task_error', {
                            'task_id': web4ai_task_id,
                            'error': status.get('error'),
                            'processed_by': 'ultimate_agent'
                        })
                        break
                
                await asyncio.sleep(2)  # Check every 2 seconds
                
        except Exception as e:
            self.logger.error(f"Task monitoring failed: {e}")
    
    async def _award_task_completion_tokens(self, task_id: str, task_status: Dict[str, Any]):
        """Award PAIN tokens for completed tasks"""
        try:
            if self.blockchain_manager and hasattr(self.blockchain_manager, 'smart_contract_manager'):
                # Calculate reward based on task complexity and resources used
                base_reward = 1.0  # Base PAIN reward
                
                # Bonus for AI tasks
                if task_status.get('ai_workload'):
                    base_reward *= 2.0
                
                # Bonus for GPU usage
                if task_status.get('gpu_used'):
                    base_reward *= 1.5
                
                # Execute smart contract to award tokens
                result = self.blockchain_manager.execute_smart_contract(
                    'task_rewards',
                    'claimReward',
                    {
                        'amount': base_reward,
                        'task_id': task_id,
                        'agent_id': self.web4ai_node.node_id
                    }
                )
                
                if result.get('success'):
                    self.logger.info(f"Awarded {base_reward} PAIN tokens for task {task_id}")
                    
                    # Update local token balance
                    self.token_manager.add_pending_reward(task_id, base_reward)
                
        except Exception as e:
            self.logger.error(f"Token award failed: {e}")
    
    async def _local_inference(self, model_name: str, input_data: Any) -> Dict[str, Any]:
        """Perform local inference using Ultimate Agent's AI manager"""
        try:
            if not self.ai_manager or not hasattr(self.ai_manager, 'run_inference'):
                return {'success': False, 'error': 'AI manager not available'}
            
            result = self.ai_manager.run_inference(model_name, input_data)
            
            return {
                'success': True,
                'result': result,
                'model': model_name,
                'processing_time': 0.1  # Placeholder
            }
            
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def _estimate_compute_power(self) -> float:
        """Estimate compute power"""
        import psutil
        cpu_count = psutil.cpu_count(logical=True)
        base_power = cpu_count * 2.5e9  # 2.5 GHz per core estimate
        
        if getattr(self.ai_manager, 'gpu_available', False):
            base_power *= 10  # GPU multiplier
        
        return base_power
    
    def _get_memory_gb(self) -> float:
        """Get available memory in GB"""
        import psutil
        try:
            return psutil.virtual_memory().total / (1024**3)
        except:
            return 8.0
    
    def _get_compute_resources(self) -> Dict[str, Any]:
        """Get compute resource information"""
        import psutil
        
        try:
            return {
                'cpu_cores': psutil.cpu_count(logical=True),
                'memory_gb': self._get_memory_gb(),
                'gpu_available': getattr(self.ai_manager, 'gpu_available', False),
                'disk_space_gb': psutil.disk_usage('/').total / (1024**3)
            }
        except:
            return {
                'cpu_cores': 4,
                'memory_gb': 8.0,
                'gpu_available': False,
                'disk_space_gb': 100.0
            }
    
    def get_ultimate_status(self) -> Dict[str, Any]:
        """Get comprehensive Ultimate Agent status"""
        status = {
            'web4ai_domain': self.web4ai_domain,
            'ultimate_agent_type': getattr(self.ultimate_agent, 'agent_type', 'unknown'),
            'components_available': {},
            'p2p_integration': False,
            'blockchain_integration': False,
            'security_integration': False
        }
        
        # Check component availability
        if self.ai_manager:
            status['components_available']['ai_manager'] = True
            status['models_available'] = list(getattr(self.ai_manager, 'models', {}).keys())
        
        if self.blockchain_manager:
            status['blockchain_integration'] = True
            status['components_available']['blockchain_manager'] = True
            status['token_balances'] = self.blockchain_manager.get_balance()
        
        if self.security_manager:
            status['security_integration'] = True
            status['components_available']['security_manager'] = True
            status['security_status'] = self.security_manager.get_security_status()
        
        if self.task_scheduler:
            status['components_available']['task_scheduler'] = True
        
        if self.p2p_integration:
            status['p2p_integration'] = True
            status['p2p_status'] = self.p2p_integration.get_p2p_status()
        
        return status

# Token management specifically for Ultimate Agent integration
class TokenManager:
    """Enhanced token management for Ultimate Agent + Web4ai"""
    
    def __init__(self, bridge: UltimateAgentWeb4aiBridge):
        self.bridge = bridge
        self.pending_rewards = {}
        self.earned_tokens = 0.0
        self.token_history = []
    
    def add_pending_reward(self, task_id: str, amount: float):
        """Add pending reward for task completion"""
        self.pending_rewards[task_id] = {
            'amount': amount,
            'timestamp': time.time(),
            'status': 'pending'
        }
    
    async def claim_all_rewards(self) -> float:
        """Claim all pending PAIN token rewards"""
        total_claimed = 0.0
        
        if self.bridge.blockchain_manager:
            try:
                # Execute smart contract to claim rewards
                result = self.bridge.blockchain_manager.execute_smart_contract(
                    'task_rewards',
                    'withdrawRewards',
                    {'amount': sum(r['amount'] for r in self.pending_rewards.values())}
                )
                
                if result.get('success'):
                    for task_id, reward in self.pending_rewards.items():
                        total_claimed += reward['amount']
                        reward['status'] = 'claimed'
                        
                        self.token_history.append({
                            'task_id': task_id,
                            'amount': reward['amount'],
                            'claimed_at': time.time()
                        })
                    
                    self.earned_tokens += total_claimed
                    self.pending_rewards.clear()
                    
            except Exception as e:
                logging.error(f"Token claim failed: {e}")
        
        return total_claimed
    
    def get_token_status(self) -> Dict[str, Any]:
        """Get token status"""
        return {
            'earned_tokens': self.earned_tokens,
            'pending_rewards': sum(r['amount'] for r in self.pending_rewards.values()),
            'pending_count': len(self.pending_rewards),
            'total_history': len(self.token_history)
        }

# Governance management for decentralized control
class GovernanceManager:
    """Governance system for Web4ai + Ultimate Agent network"""
    
    def __init__(self, bridge: UltimateAgentWeb4aiBridge):
        self.bridge = bridge
        self.proposals = {}
        self.votes = {}
    
    async def create_proposal(self, proposal_data: Dict[str, Any]) -> str:
        """Create governance proposal"""
        proposal_id = f"ultimate-prop-{uuid.uuid4().hex[:8]}"
        
        proposal = {
            'id': proposal_id,
            'title': proposal_data['title'],
            'description': proposal_data['description'],
            'type': proposal_data['type'],
            'proposed_by': self.bridge.web4ai_node.node_id,
            'created_at': time.time(),
            'voting_ends': time.time() + 7 * 24 * 3600,  # 7 days
            'votes_for': 0,
            'votes_against': 0
        }
        
        self.proposals[proposal_id] = proposal
        
        # Broadcast to network
        await self.bridge.web4ai_node.broadcast_message('ultimate_governance_proposal', {
            'action': 'new_proposal',
            'proposal': proposal
        })
        
        return proposal_id
    
    async def vote_on_proposal(self, proposal_id: str, vote: bool, voting_power: float):
        """Vote on proposal"""
        if proposal_id not in self.proposals:
            raise ValueError(f"Proposal {proposal_id} not found")
        
        proposal = self.proposals[proposal_id]
        
        # Record vote
        vote_key = f"{self.bridge.web4ai_node.node_id}:{proposal_id}"
        self.votes[vote_key] = {
            'voter': self.bridge.web4ai_node.node_id,
            'proposal_id': proposal_id,
            'vote': vote,
            'voting_power': voting_power,
            'timestamp': time.time()
        }
        
        # Update proposal counts
        if vote:
            proposal['votes_for'] += voting_power
        else:
            proposal['votes_against'] += voting_power
        
        # Broadcast vote
        await self.bridge.web4ai_node.broadcast_message('ultimate_governance_proposal', {
            'action': 'vote_cast',
            'proposal_id': proposal_id,
            'vote': vote,
            'voter': self.bridge.web4ai_node.node_id
        })