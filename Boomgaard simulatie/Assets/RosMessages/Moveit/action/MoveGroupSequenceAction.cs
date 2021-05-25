using System.Collections.Generic;
using Unity.Robotics.ROSTCPConnector.MessageGeneration;


namespace RosMessageTypes.Moveit
{
    public class MoveGroupSequenceAction : Action<MoveGroupSequenceActionGoal, MoveGroupSequenceActionResult, MoveGroupSequenceActionFeedback, MoveGroupSequenceGoal, MoveGroupSequenceResult, MoveGroupSequenceFeedback>
    {
        public const string RosMessageName = "moveit_msgs/MoveGroupSequenceAction";

        public MoveGroupSequenceAction() : base()
        {
            this.action_goal = new MoveGroupSequenceActionGoal();
            this.action_result = new MoveGroupSequenceActionResult();
            this.action_feedback = new MoveGroupSequenceActionFeedback();
        }

        public override List<byte[]> SerializationStatements()
        {
            var listOfSerializations = new List<byte[]>();
            listOfSerializations.AddRange(this.action_goal.SerializationStatements());
            listOfSerializations.AddRange(this.action_result.SerializationStatements());
            listOfSerializations.AddRange(this.action_feedback.SerializationStatements());

            return listOfSerializations;
        }

        public override int Deserialize(byte[] data, int offset)
        {
            offset = this.action_goal.Deserialize(data, offset);
            offset = this.action_result.Deserialize(data, offset);
            offset = this.action_feedback.Deserialize(data, offset);

            return offset;
        }

    }
}
